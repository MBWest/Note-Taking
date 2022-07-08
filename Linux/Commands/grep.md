# Grep

Print lines that match patterns

## Grep Basics

## Options

| **Command**   | **Description**   |
| --------------|-------------------|
| **Option** |
| `-i` | Makes grep search case insensitve  |
| `-w` | Ensures that grep only matches whole words rather than fragments located inside other words |
| `-r` | Perfoms a recursive search, which will include all files under a directory, subdirectories, and their files, and so on  |
| `-n` | Lables each line with the applicable line number |
| `-c` | Counts how many times the grep commands finds the requested pattern |
| `-A` | Gives x number of lines after each pattern found |
| `-B` | Gives x number of lines before each pattern found |
| `-C` | Gives x number of lines before and after each pattern found |
| `-E` | Same as using egrep |
| `-v` | Show all results that do not match the specified pattern |

## Grep and Regular Expressions

| **Command**   | **Description**   |
| --------------|-------------------|
| **Grep and Regular Expressions** |
| `.` | Matches any single character |
| `?` | Matches 1 or less the preceding pattern |
| `^` | Matches the start of a line |
| `$` | Matches the end of a line |
| `[abc]` | Matches any character in the set |
| `[^abc]` | Matches any character NOT in the set |
| `[A-Z]` | Matches characters in a range |
| `a{1}` | Matches the preceding letter repeating {x} times (a{3} = aaa) |
| `*` | Repeat previous expression 0 or more times |
| `\*` | Escape meta-characters |

## Examples

| **Command**   | **Description**   |
| --------------|-------------------|
| **Examples** |
| `grep "chicken" animals.txt` | Prints each line from the animals.txt file that contains the pattern "chicken" |
| `grep bob wordlist.txt` | Searches through the wordlist.txt file for any string that matches the pattern 'bob' |
| `grep -v e wordlist.txt \| less` |  Searches through the wordlist.txt for words without the letter 'e' and pipes the results to the less command |
| `grep error /var/log/*.log` | Searches multiple files for the pattern 'error' |
| `grep error -A 1 -B 3 /var/log/*.log` | Searches multiple files for the pattern 'error', also shows you 1 line aftern the match and 3 lines before the match |
| `grep -v e random-words.txt` | Searches through the wordlist.txt for words without the letter 'e'  |
| `grep -v e random-words.txt \| sort` | Searches through the wordlist.txt for words without the letter 'e', then pipes the results to the sort command to have the results appear alphabetically |
| `grep -v e random-words.txt \| sort \| uniq` | Searches through the wordlist.txt for words without the letter 'e', then pipes the results to the sort command to have the results appear alphabetically, then pipes the results to the uniq q command to remove any adjacent duplicate lines |
| `grep -v e random-words.txt \| sort \| uniq \| wc -l` | Searches through the wordlist.txt for words without the letter 'e', then pipes the results to the sort command to have the results appear alphabetically, then pipes the results to the uniq command to remove any adjacent duplicate lines, then pipes the results the wordcount (wc) command with the -l options to only show the count of lines |
| `grep www1-google-analytics.com access.log \| head -n 1` |
| `grep www1-google-analytics.com access.log` | extract lines that contain the string www1-google-analytics.com. |