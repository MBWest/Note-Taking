# ps

List processes

## Examples

| **Command**   | **Description**   | 
| --------------|-------------------|
| **Standard Syntax Examples** |
| `ps aux` or `ax` | See every process on the system |
| `ps -U root -u root u` | See every process owned by root |
| **BSD Syntax Examples** |
| `ps -e` or `-ef` or `-eF` or `-ely` | See every process on the system |
| **Process Tree Examples** |
| `ps -ejH` or `axjf` or `eh` | Print a process tree |
|**Thread Information Examples** |
| `ps -eLf` or `axms` | Get information about threads |