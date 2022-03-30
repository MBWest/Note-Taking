import re
# The above command imports the regex library


# ---------- Regex ----------
# Regex example
string = "'I AM NOT YELLING', she said. Though we knew it to not be true."
print(string)
# Create a new variable and use the sub (substitute function) on the object that we imported at the top of the script (import re)
# re.sub(match, replace, and the string to manipulate)
# Rules in regex are contained in [] brackets. Example; [ABC...] or [A-Z]; Use back slashes to escape (\); Use " " to remove spaces
# To replace anything but the following items begin the match section with a ^. Example '[^0-9]' will replace everything but 0-9 numbers

new = re.sub('[.,\']', '', string)
print(new)
