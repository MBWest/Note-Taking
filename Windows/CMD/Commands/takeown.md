# takeown

- Forces ownership change on files/folders
- Used by administrators to regain access to files/folder locations

---

## Examples

| **Command** | **Description** |
|-------------|-----------------|
| `takeown /f lostfile` | Current user takes ownership of lostfile |
| `takeown /f c:\windows\*.txt /d` | Take ownership of .txt and ignore prompts |
| `takeown /f c:\windows /r /d` | Recursively take ownership of windows dir |