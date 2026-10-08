#!/usr/bin/env python3
"""
Extrator de Claims da OpenAPI V2 Real (LAB TWS 10.2.8)
Arquivo fonte: data/lab/WA_API3_v2.json (212 paths, 276 operações)
Gera: data/lab/openapi_v2_claims.jsonl
"""

import json
import os
import re

def resolve_ref(ref, spec):
    parts = ref.strip("#/").split("/")
    cur = spec
    for p in parts:
        cur = cur.get(p, {})
    return cur

def describe_schema(schema, spec, depth=0):
    if depth > 3:
        return "{...}"
    if not schema:
        return ""
    if "$ref" in schema:
        resolved = resolve_ref(schema["$ref"], spec)
        ref_name = schema["$ref"].split("/")[-1]
        if depth > 1:
            return ref_name
        return f"{ref_name}: {describe_schema(resolved, spec, depth+1)}"
    
    # Handle oneOf / anyOf / allOf
    for combo in ("oneOf", "anyOf", "allOf"):
        if combo in schema:
            sub = [describe_schema(s, spec, depth+1) for s in schema[combo][:3]]
            return f"{combo}({', '.join(sub)})"
    
    stype = schema.get("type", "object")
    if isinstance(stype, list):
        stype = "/".join(stype)
    if stype == "array":
        items = schema.get("items", {})
        return f"array[{describe_schema(items, spec, depth+1)}]"
    if stype == "object" or "properties" in schema:
        props = schema.get("properties", {})
        if not props:
            return "object"
        prop_desc = []
        for p_name, p_schema in list(props.items())[:6]:
            pt = p_schema.get("type", "any")
            if isinstance(pt, list):
                pt = "/".join(pt)
            prop_desc.append(f"{p_name} ({pt})")
        return "{" + ", ".join(prop_desc) + ("..." if len(props) > 6 else "") + "}"
    return str(stype)

def main():
    json_path = "data/lab/WA_API3_v2.json"
    out_path = "data/lab/openapi_v2_claims.jsonl"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    with open(json_path, "r", encoding="utf-8") as f:
        spec = json.load(f)

    paths = spec.get("paths", {})
    claims = []
    idx = 1

    for path, methods in sorted(paths.items()):
        for method, details in methods.items():
            if method.lower() not in ("get", "post", "put", "delete", "patch"):
                continue
            if not isinstance(details, dict):
                continue

            op_id = details.get("operationId", f"{method.lower()}_{path.replace('/', '_')}")
            summary = details.get("summary", "").strip() or details.get("description", "").strip() or f"{method.upper()} {path}"
            description = details.get("description", "").strip()
            tags = details.get("tags", ["V2 APIs"])

            # Parameters (both from path level and operation level)
            params = list(methods.get("parameters", [])) + list(details.get("parameters", []))
            path_params = []
            query_params = []
            header_params = []

            for p in params:
                if "$ref" in p:
                    p = resolve_ref(p["$ref"], spec)
                p_in = p.get("in", "")
                p_name = p.get("name", "")
                p_req = "obrigatório" if p.get("required") else "opcional"
                p_desc = p.get("description", "").strip()
                p_type = p.get("schema", {}).get("type", "string") if "schema" in p else p.get("type", "string")
                entry = f"`{p_name}` ({p_type}, {p_req})" + (f": {p_desc}" if p_desc else "")
                
                if p_in == "path":
                    path_params.append(entry)
                elif p_in == "query":
                    query_params.append(entry)
                elif p_in == "header":
                    header_params.append(entry)

            # Request Body
            req_body_str = ""
            req_body = details.get("requestBody", {})
            if "$ref" in req_body:
                req_body = resolve_ref(req_body["$ref"], spec)
            if req_body:
                content = req_body.get("content", {})
                for c_type, c_val in content.items():
                    schema = c_val.get("schema", {})
                    s_desc = describe_schema(schema, spec)
                    req_desc = req_body.get("description", "").strip()
                    req_body_str = f"Formato: {c_type}. Schema: {s_desc}"
                    if req_desc:
                        req_body_str += f" ({req_desc})"
                    break

            # Responses
            responses = details.get("responses", {})
            resp_list = []
            for r_code, r_val in sorted(responses.items()):
                if "$ref" in r_val:
                    r_val = resolve_ref(r_val["$ref"], spec)
                r_desc = r_val.get("description", "").strip()
                r_content = r_val.get("content", {})
                r_schema_str = ""
                for ct, cv in r_content.items():
                    if "schema" in cv:
                        rs = cv["schema"]
                        r_schema_str = f" [retorna {describe_schema(rs, spec, depth=1)}]"
                    break
                resp_list.append(f"{r_code}: {r_desc}{r_schema_str}")

            # Montagem do texto do claim (conciso, técnico, assertivo)
            claim_parts = []
            claim_parts.append(f"A API REST v2 do HCL Workload Automation (HWA 10.2.8) disponibiliza o endpoint `{method.upper()} {path}`.")
            if summary:
                s_clean = summary.rstrip(".")
                claim_parts.append(f"Finalidade: {s_clean}.")
            if description and description != summary:
                # Sanitizar quebras de linha excessivas
                clean_desc = re.sub(r'\s+', ' ', description).strip().rstrip(".")
                claim_parts.append(f"Detalhes: {clean_desc}.")
            if path_params:
                claim_parts.append("Parâmetros de Path: " + "; ".join(path_params) + ".")
            if query_params:
                claim_parts.append("Parâmetros de Consulta (Query): " + "; ".join(query_params[:8]) + ("..." if len(query_params) > 8 else "") + ".")
            if req_body_str:
                claim_parts.append(f"Corpo da Requisição (Request Body): {req_body_str}.")
            if resp_list:
                claim_parts.append("Respostas HTTP documentadas: " + "; ".join(resp_list[:6]) + ".")

            claim_text = " ".join(claim_parts)
            tag_str = ", ".join(tags)
            clean_summary = summary.rstrip(".")
            title = f"REST API v2: {method.upper()} {path} - {clean_summary}"
            if len(title) > 120:
                title = f"REST API v2: {method.upper()} {path} - {clean_summary[:80]}"

            record = {
                "id": f"lab-openapi-{idx:03d}",
                "category": "API REST v2 & Integracao",
                "title": title,
                "claim": claim_text,
                "method": method.upper(),
                "path": path,
                "tags": tags,
                "source": "OpenAPI WA_API3_v2.json (LAB TWS 10.2.8)"
            }
            claims.append(record)
            idx += 1

    with open(out_path, "w", encoding="utf-8") as f:
        for c in claims:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")

    print(f"Sucesso: {len(claims)} claims de operações REST gerados em {out_path}.")

if __name__ == "__main__":
    main()
