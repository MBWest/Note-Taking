# Grep

Print lines that match patterns

## Grep Basics

The **grep** command searches for patterns in each file's content. **Grep** will print each line that matches a pattern we provide
- *Example* > grep "chicken" animals.txt
	- Prints each line from the animals.txt file that contains the pattern "chicken"

## Grep Options

- **-i** - Makes grep search case insensitve
- **-w** - Ensures that grep only matches whole words rather than fragments located inside other words
- **-r** - Perfoms a recursive search, which will include all files under a directory, subdirectories, and their files, and so on 
- **-n** - Lables each line with the applicable line number
- **-c** - Counts how many times the grep commands finds the requested pattern
- **-A** - Gives x number of lines after each pattern found
- **-B** - Gives x number of lines before each pattern found
- **-C** - Gives x number of lines before and after each pattern found
- **-E** - Same as using egrep

## Grep and Regular Expressions

- **.**- Matches any single character
- **?**- Matches 1 or less the preceding pattern
- **^** - Matches the start of a line
- **$** - Matches the end of a line
- **[abc]** - Matches any character in the set
- **[^abc]**- Matches any character NOT in the set
- **[A-Z]** - Matches characters in a range
- **a{1}** - Matches the preceding letter repeating {x} times (a{3} = aaa)
- * - Repeat previous expression 0 or more times
- **\*** - Escape meta-characters

## Examples

- **grep bob wordlist.txt** - 
- **grep -v e wordlist.txt | less** - 
- **grep error /var/log/*.log** - 
- **grep error -A 1 -B 3 /var/log/*.log** - 
- **grep -v e random-words.txt** - 
- **grep -v e random-words.txt | sort** - 
- **grep -v e random-words.txt | sort | uniq** - 
- **grep -v e random-words.txt | sort | uniq | wc -l** - 