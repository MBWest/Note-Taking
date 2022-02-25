# tee

The tee program rads standard input and copies it both to standard output AND to a file. This allows the user to capture information part of the way through a pipeline, without interrupting the flow.
- *Example* > command1 | **tee** file.txt | command2
