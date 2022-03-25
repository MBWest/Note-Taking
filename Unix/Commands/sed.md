# sed

Stream editor for filtering and transforming text
- Operates on text as it flows by and not on the whole file all at once. Unless the `g` option is set, sed will only replace the first instance of the pattern.

## Resources  

**Sed manual:** https://www.gnu.org/software/sed/manual/sed.html

## Format

sed [OPTIONS] {script-only-if-no-other-script} [input-file]

## Examples

- **man sed** - Opens up the sed man page
- **sed 's/Suite/Ste/' sample.txt** - Substitutes every occurence of 'Suite' with the abbreviation 'Ste' in the sample.txt file
- **echo Suite Suite | sed 's/Suite/Ste/'** - Substitutes the first instance 'Suite' with 'Ste'
- **echo Suite Suite | sed 's/Suite/Ste/g'** - Substitutes every instance of 'Suite' with 'Ste' using the 'g' option
- **sed '$s/Suite/Ste/' sample.txt** - Substitutes the last instance 'Suite' with 'Ste'
- **sed '/Suite/d' sample.txt** - Deletes every line that has the instance of 'Suite' ocurring using the 'd' option
- **sed '/ee/ s/Suite/Ste/g' sample.txt** - Substitues every instance of 'Suite' with 'Ste' on every line that has an 'ee' occurance
- **sed 's/$/\n/g' sample.txt | sed 's/,/\n/g'** -
- **sed -e 's/$/\n/g' -e 's/,/\n/g' sample.txt** -