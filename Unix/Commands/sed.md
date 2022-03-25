# sed

Stream editor for filtering and transforming text

## Resources  

**Sed manual:** https://www.gnu.org/software/sed/manual/sed.html

## Format

sed [OPTIONS] {script-only-if-no-other-script} [input-file]

## Examples

- **man sed** -
- **cat sample.txt** -
- **sed 's/Suite/Ste/' sample.txt** -
- **echo Suite Suite | sed 's/Suite/Ste/'** -
- **echo Suite Suite | sed 's/Suite/Ste/g'** -
- **sed '$s/Suite/Ste/g' sample.txt** -
- **sed '/Suite/d' sample.txt** -
- **sed '/ee/ s/Suite/Ste/g' sample.txt** -
- **sed 's/$/\n/g' sample.txt | sed 's/,/\n/g'** -
- **sed -e 's/$/\n/g' -e 's/,/\n/g' sample.txt** -