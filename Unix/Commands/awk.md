# awk

## Resources

**AWK manual:** https://www.gnu.org/software/gawk/manual/gawk.html

## Examples

- **awk '/midnitemeerkats/ {print $1, $3, $7}' access.log**
    - **/midnitemeerkats/** - only process lines that contain the string midnitemeerkats
    - **print** - print the following fields
    - **$1** - first field (timestamp)
    - **$3** - third field (requesting client)
    - **$7** - seventh field (requested URL)
    access.log - The file to process
- **awk '/www1-google-analytics.com/ {print $3}' access.log | sort -u**
    - **awk '/www1-google-analytics.com/ {print $3};' access.log** - print the third field (the requesting IP address) for lines that contain www1-google-analytics.com in the file access.log
    - **sort -u** - sort the list of IP addresses, returning unique values
