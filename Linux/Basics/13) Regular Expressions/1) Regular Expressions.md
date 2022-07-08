# Linux - Regular Expressions

> ## **What is a Regular Expression (regex)**
- Sequence of characters that define a `search pattern` for text
- Standalone topic
    - Even though regex is taught here using grep, regex can be used in many situations with many different tools performing the pattern search 
        - Notepad++, programming languages, other nix utilities, etc… 

> ## **grep [OPTIONS] PATTERN [FILE...] || grep [OPTIONS] [-e PATTERN|-f FILE] [FILE...]**
- `-E` - Interpret PATTERN as an extended regex
- `-i` - ignore case
- `-v` - invert match; to select non-matching lines
- `-B NUM`  - print NUM lines of leading context before matches
- `-A NUM`  - print NUM lines of trailing context after matches
- `-r or -R`   - read all files under each directory
- `-e PATTERN` - use PATTERN as the pattern
    - This can be used to specify multiple search patterns

> ## **Literal Characters**
- Normal characters are referred to as `literal characters`
    - Literally the character `g` followed by literally the character `a` followed by literally the character `l` ...

```text

Regex - /galaxy/g

   ---Body of text---             ---Output---
|----------------------|    |----------------------|
|                      |    |                      |
| A long time ago in a |    |       galaxy         |
| galaxy far far       |    |                      |
| away...              |    |                      |
|                      |    |                      |
|                      |    |                      |
|                      |    |                      |
|                      |    |                      |
|                      |    |                      |
|----------------------|    |----------------------|
```

----

> ## **Metacharacters**
- Used to create `generalized` search patterns 
    - `.` - a metacharacter that represents any character except a newline

```text

Regex - /g../g

   ---Body of text---             ---Output---
|----------------------|    |----------------------|
|                      |    |                      |
| A long time ago in a |    |     'g t'            |
| galaxy far far       |    |     'go '            |
| away...              |    |     'gal'            |
|                      |    |                      |
|                      |    |                      |
|                      |    |                      |
|                      |    |                      |
|                      |    |                      |
|----------------------|    |----------------------|
```
---

> ## **Bracket Expression**
- list of characters enclosed in `[ … ]`
- Matches any single character in that list 
- [`^`...] - A caret in the first position signifies negation
- Most `metacharacters lose` their `special meaning` inside bracket expressions
    - To include a literal `]` in a bracket expression; place it `first`
    - To include a literal `^` in a bracket expression; place it `anywhere except first`
    - To include a literal `-` in a bracket expression; place it `last`

---

> ## **Range Expression**
- Within a bracket expression; two characters separated by a hyphen
    - Matches any character that sorts between the two in the range

```text

Regex - /[e-h]/g

   ---Body of text---             ---Output---
|----------------------|    |----------------------|
|                      |    |                      |
| A long time ago in a |    |     'g'              |
| galaxy far far       |    |     'e'              |
| away...              |    |     'g'              |
|                      |    |     'g'              |
|                      |    |     'f'              |
|                      |    |     'f'              |
|                      |    |                      |
|                      |    |                      |
|----------------------|    |----------------------|
```

---

> ## **Named Character Class**
- Predefined characters `within bracket expressions`

| **Class**| **Meaning** |
|:----------:|-----------|
| `[:alpha:]`  | Any letter, [A-Za-z] |
| `[:upper:]`  | Any uppercase letter, [A-Z] |
| `[:lower:]`  | Any lowercase letter, [a-z] |
| `[:digit:]`  | Any digit, [0-9] |
| `[:alnum:]`  | Any alphanumeric character, [A-Za-z0-9] |
| `[:xdigit:]` | Any hexadecimal digit, [0-9A-Fa-f] |
| `[:space:]`  | A tab, new line, vertical tab, form feed, carriage return, or space |
| `[:blank:]`  | A space or a tab. |
| `[:print:]`  | Any printable character |
| `[:punct:]`  | Any punctuation character: ! ' # S % & ' ( ) * + , - . / : ; < = > ? @ [ / ] ^ _ { \| } ~ |
| `[:graph:]`  | Any character defined as a printable character except those defined as part of the space  |character class
| `[:word:]`  |	Continuous string of alphanumeric characters and underscores. |
| `[:ascii:]` |  ASCII characters, in the range: 0-127 |
| `[:cntrl:]` |  Any character not part of the character classes: [:upper:], [:lower:], [:alpha:], [:digit:], [:punct:], [:graph:], [:print:], [:xdigit:] |



```text

Regex - /[:upper:]/g

   ---Body of text---             ---Output---
|----------------------|    |----------------------|
|                      |    |                      |
| A long time ago in a |    |     'A'              |
| galaxy far far       |    |                      |
| away...              |    |                      |
|                      |    |                      |
|                      |    |                      |
|                      |    |                      |
|                      |    |                      |
|                      |    |                      |
|----------------------|    |----------------------|
```

---

> ## **Regex Special Characters**

| **Character** | **Meaning** |	**Example** |
|:-------------:|-------------|-------------|
| `*` 	| Match zero, one or more of the previous |	Ah* matches "Ahhhhh" or "A"| 
| `?` 	| Match zero or one of the previous |	Ah? matches "Al" or "Ah"| 
| `+` 	| Match one or more of the previous |	Ah+ matches "Ah" or "Ahhh" but not "A"| 
| `\` 	| Used to escape a special character |	Hungry\? matches "Hungry?"| 
| `.` 	| Wildcard character, matches any character |	do.* matches "dog", "door", "dot", etc.| 
| `( )` |	Group characters |	See example for \| | 
| `[ ]` |	Matches a range of characters |[cbf]ar matches "car", "bar", or "far" 
| | | [0-9]+ matches any positive integer 
| | | [a-zA-Z] matches ascii letters a-z (uppercase and lower case) 
| | | [^0-9] matches any character not 0-9.| 
| `\|` 	| Matches previous OR next character/group |	(Mon\|Tues)day matches "Monday" or "Tuesday"| 
| `{ }` | 	Matches a specified number of occurrences of the previous |	[0-9]{3} matches "315" but not "31" |
| | | [0-9]{2,4} matches "12", "123", and "1234" |
| | | [0-9]{2,} matches "1234567..."| 
| `^` |	Beginning of a string. Or within a character range [] negation.  |	^http matches strings that begin with http, such as a url. 
| | | [^0-9] matches any character not 0-9.| 
| `$` |	End of a string. |	ing$ matches "exciting" but not "ingenious"| 
| `\<` | Match the empty string at the beginning of a word | | 
| `\>` | Match the empty string at the end of a word | |
