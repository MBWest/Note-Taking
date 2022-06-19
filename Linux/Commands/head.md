# head

## Format

`head [filename]`

## Examples

| **Command**   | **Description**   |
| --------------|-------------------|
| **Examples** |
| `head [filename]` | Prints a portion of a file starting at the beginning of the file (Default 10 lines) |
| `head -n 21 [filename]` | Prints the first 21 lines of the file |
| `--lines 21` | Equal to *-n 21* |
| `-21` | Equal to *--lines 21* or *-n 21* |
| `head -c 8 [filename]` | Prints the first 8 bytes of the file |