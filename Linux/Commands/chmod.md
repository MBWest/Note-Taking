# chmod

| **Command**   | **Description**   |
| --------------|-------------------|
| **chmod** |
| `chmod` | Change the permissions of a file or directory. |
| **who** |
| `u` | User (The owner of the file). |
| `g` | Group (Members of the group the file belongs to). |
| `o` | Others (The 'World'). |
| `a` | All of the above. |
| **What** |
| `Minus Sign (-)` | Removes the permission. |
| `Plus Sign (+)` | Grants the permission. |
| `Equal Sign (=)` | Set a permission and removes others. |
| **Which** |
| `r` | The read permissions. |
| `w` | The write permissions. |
| `x` | The execute permissions. |

## Examples

| **Command**   | **Description**   |
| --------------|-------------------|
| **Examples** |
| `chmod a= hello.txt` | Remove all permissions for all users. |
| `chmod g+w file.txt` | Add write permissions to the group. |
| `chmod a-w file.txt` | Remove write permissions from all. |


## chmod octals

Chmod also supports octal number (base 8). Each digit in an octal number represents 3 binary digits

| **R** | **W**  | **X**  |
|-------|--------|--------|
| `2^2`| `2^1` | `2^0` |
|  4| 2 | 1 |

| **Octal**  | **Binary**  | **File Mode**  |
|------------|-------------|----------------|
|`0`| 000 | - - - |
|`1`| 001 | - -x |
|`2`|  010| -w- |
|`3`|  011| -wx |
|`4`|  100| r- - |
|`5`| 101 |r-x |
|`6`|110  |rw-  |
|`7`| 111  |rwx  |