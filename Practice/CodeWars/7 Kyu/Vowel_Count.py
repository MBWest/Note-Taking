# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    count = 0
    vowels = ["a", "e", "i", "o", "u"]
    for i in sentence:
        if i in vowels:
            count += 1
    return count

# Top Answer

def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")