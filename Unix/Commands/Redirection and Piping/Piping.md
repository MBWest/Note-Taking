# Piping

## Piping vs Redirecting

**>** Connects a command to some file

**|** Connets a command to another command

## Piping (|)

Pipe the standard output from one command into the standard input of another command using the (**|**) 

### Examples

- **ls -l /etc/ | less** - Pipes the output from the `ls -l /etc/` into the less command
- **ls -l /etc/ | head -n 20 | tail -n 5** - Pipes the output from the `ls -l /etc/` into the head command and pipes that output into the tail command
- **find / -name 'sample.txt' | less** - Pipes the output from the `find / -name 'sample.txt'` into the less command
- **find / -name 'sample.txt' |& less** - Pipes the `find / -name 'sample.txt'` into the less command with standard error