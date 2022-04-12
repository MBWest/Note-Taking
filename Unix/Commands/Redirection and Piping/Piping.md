# Piping

| **Command**   | **Description**   |
| --------------|-------------------|
| **Piping vs Redirection** |
| `>` | Connects a command to some file |
| `\|` | Pipe the standard output from one command into the standard input of another command |
| **Piping** |
| `ls -l /etc/ \| less` | Pipes the output from the ls -l /etc/ into the less command |
| `ls -l /etc/ \| head -n 20 \| tail -n 5` | Pipes the output from the ls -l /etc/ into the head command and pipes that output into the tail command |
| `find / -name 'sample.txt' \| less` | Pipes the output from the find / -name 'sample.txt' into the less command |
| `find / -name 'sample.txt' \|& less` | Pipes the find / -name 'sample.txt' into the less command with standard error |