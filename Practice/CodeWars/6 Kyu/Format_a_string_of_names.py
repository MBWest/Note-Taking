# Given: an array containing hashes of names

# Return: a string formatted as a list of names separated by commas
# except for the last two names, which should be separated by an ampersand.

def namelist(names):
    string = ""
    if len(names) != 0:
        arr = []
        for i in range(0, len(names) -1):
            arr.append(names[i]['name'])
        string = ', '.join(arr)
        string += ' & ' + names[-1]['name'] if string != '' else names[-1]['name']
    return string


# Example:

print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]))
# returns 'Bart, Lisa & Maggie'

print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ]))
# returns 'Bart & Lisa'

print(namelist([ {'name': 'Bart'} ]))
# returns 'Bart'

print(namelist([]))
# returns ''
# Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.


# CodeWars top Solution -------------------------------------------------

def namelist(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]),
                                names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''

# Another CodeWars top Solution -------------------------------------------------
def namelist(names):
    if len(names)==0: return ''
    if len(names)==1: return names[0]['name']
    return ', '.join([n['name'] for n in names[:-1]]) + ' & ' + names[-1]['name']
