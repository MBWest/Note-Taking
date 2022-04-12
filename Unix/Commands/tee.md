# tee

The tee program rads standard input and copies it both to standard output AND to a file. This allows the user to capture information part of the way through a pipeline, without interrupting the flow.

| **Command**   | **Description**   |
| --------------|-------------------|
| **Example** |
| `command1 | tee file.txt | command2` | Show the output from command 1 and parse it to command 2 |