# cat

Concatenate files and print on the standard output

---

> ## **Example** 

| **Command**   | **Description**   |
| --------------|-------------------|
| **Piping vs Redirection** |
| `cat *filename` | Concatenates and prints the contents of a file. |
| `cat *filename1 filename2` | Displays the contents of both filename1 and filename2. |
| `cat *filename.txt* -n` | Displays the contents of the file with each line having a number assosiated with it. |
| `cat *filename.txt* -b` | Displays the contents of the file with each *non-empty* line having a number assosiated with it |
| **Redirection** |
| `cat *filename > newfilename` | Concatenates and redirects the contents of filename into newfilename. |
| `cat *filename1 filename2 > newfilename` | Concatenates and redirects the contents of filename1 and filename2 into newfilename. |
| `cat > newfile.txt` | Allows you to enter text into the newfile.txt through standard input displayed in the terminal. |