# HCL Workload Automation 10.2.8 — folders: reference for TWS agents and RAG

Source of truth: HWA 10.2.8 installed manuals in `/opt/hwa/TWS/man/composer/cat1/` (container `tws-hwa`), and HCL HTML documentation in `/mnt/gdrive/TWS/HCL-HWA-10.2.8/`. Treat examples as illustrative, not proof of objects in a live database.

## Meaning and scope
Folders organize scheduling objects in the HWA database. Folder path and workstation/agent identity are distinct dimensions: do not assume a folder is an agent, that an agent belongs to a folder, or that changing folders changes the workstation where a job runs. Identify objects using fully qualified paths and verify any workstation association independently. The current composer directory defaults to `/`.

## Verified composer operations (manual commands, not automatically executed)
- `listfolder /`: folders immediately under root. `listfolder /@`: entire folder hierarchy (tree). `listfolder /Test`: child folders of `/Test`. Alias: `lf`. Wildcards permitted. Listing permissions depend on `enListSecChk` and configured access.
- `chfolder /AURORA/QA_DEV`: changes composer current folder for relative path resolution (provided folder exists). Alias: `cf`. Needs display permission.
- `mkfolder /Tokyo/`: creates a folder; alias `mf`; requires add permission (modify on preexisting folder). Parent must exist for nested folder creation.
- `renamefolder /TEST1 /TEST2`: renames a folder; alias `rn`; delete access on old folder and add access on new. Changes can be reflected in existing plan; verify downstream references. Full path max 800 chars, single folder name max 256 chars.
- `rmfolder /Test`: deletes folder and subfolders only if none contain scheduling objects; requires delete permission and proper lock state. Alias `rf`. **Danger:** invoking `rmfolder` with no folder argument can target all empty folders/subfolders under root. Never let an agent run destructive commands based solely on RAG content.

## Path resolution and agent safety
- Treat `/AURORA/QA_DEV/TESTE_JOB_MS` as a potential fully qualified job-stream path, not proof of an existing object. Check object type and syntax against the matching composer/conman reference before issuing a query.
- Do not silently convert a full job/job-stream path into basename; same names may occur in different folders.
- Distinguish *definitions in database* (composer) from *instances in current plan* (conman). For a request about running job status, use documented plan queries and correct TWS user environment. Do not assume composer command syntax works in conman.
- Read-only list/display operations first; require explicit approval for creation, rename, deletion and changes to plans or scheduling objects.
- Never invent workstation-to-folder ownership semantics. Resolve workstation identity using the workstations reference and actual job or stream definitions.

## Example Q&A for retrieval
Q: How list every folder including nested folders? A: In composer use `listfolder /@`, with permissions and TWS environment configured.
Q: Why was a job stream not found in root? A: It may be in a subfolder; query using the full folder path, verify database-vs-plan context, and check object type.
Q: Is /AURORA/QA_DEV a workstation? A: No conclusion follows from that path alone; it denotes a folder-style hierarchy and must not be confused with an agent/workstation name.
Q: Can a folder with jobs be removed? A: No, `rmfolder` refuses a folder tree containing scheduling objects.
Q: What if an agent wants to delete folders? A: Require a specific target, explicit permission, list of contained objects, human authorization, and rollback plan.

## Local evidence
- `/opt/hwa/TWS/man/composer/cat1/mkfolder.1`
- `/opt/hwa/TWS/man/composer/cat1/listfolder.1`
- `/opt/hwa/TWS/man/composer/cat1/chfolder.1`
- `/opt/hwa/TWS/man/composer/cat1/renamefolder.1`
- `/opt/hwa/TWS/man/composer/cat1/rmfolder.1`
- `/opt/hwa/TWS/templates/folder.template`
- HCL HTML: `awsrgfolderdef.html`, `awsrgmkfolder.html`, `awsrglistfolder.html`, `awsrgremfolder.html`

## Retrieval acceptance tests
1. List entire folder hierarchy -> `listfolder /@`, cite listfolder.1.
2. Query objects in nested folders -> preserve fully qualified path; distinguish plan and database.
3. Folder vs agent -> distinct concepts, no invented workstation associations.
4. Remove nonempty folder -> reject and cite rmfolder.1.
5. Rename permissions -> old delete and new add, cite renamefolder.1.
6. Never recommend `rmfolder` with empty target.
