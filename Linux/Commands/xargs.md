# Xargs Command

When **-exec** is used, the command is executed separatley for every single element, unlike **xargs** which builds up the input into a bundle that will be provided as an arguement to the next command. 
- find -name "*txt" -exec ls '{}' ';' **=EQUALS=** find -name ".txt" | xargs ls