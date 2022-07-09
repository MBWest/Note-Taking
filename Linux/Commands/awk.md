# awk

> ## **Resources** 

**AWK manual:** https://www.gnu.org/software/gawk/manual/gawk.html

---

> ## **Example** 

| **Command**   | **Description**   |
| --------------|-------------------|
| `awk '/midnitemeerkats/ {print $1, $3, $7}' access.log` | 
| `/midnitemeerkats/` | Only process lines that contain the string midnitemeerkats. |
| `print` | print the following fields. |
| `$` | First field (timestamp).  |
| `$3` | Third field (requesting client) |
| `$7` | Seventh field (requested URL). |
| `access.log` | The file to process. |
| **Create Custom Wordlist Example** |
| `awk '{ print "fm-"$1 }' labs/dns/namelist.txt  > falsimentis-namelist.txt` |
| `'{` | Begin an awk program; a space after { isn't necessary but it makes the Awk program easier to read. |
| `print "fm-"$1` | The awk program itself; print to the screen the string "fm-" followed by the first column in the processed file; for this example, the program will prepend "fm-" to each word in the name list. |
| `}` | End the awk program; the space isn't necessary here either, but improves readability. |
| `labs/dns/namelist.txt` | Process each line in the labs/dns/namelist.txt file. |
| `> falsimentis-namelist.txt` | Redirect the output (the print output from the awk program) to the named file. |
