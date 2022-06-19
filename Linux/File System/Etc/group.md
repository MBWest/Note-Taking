# /etc/group

User group file

## /etc/group Fields

The /etc/group file is a text file that defines the groups on the system. There is one entry per line, with the following format:

    group_name:password:GID:user_list

**The fields are as follows:**

- **group_name** - The name of the group
- **password** - The (encrypted) group password. If this field is empty, no password is needed
- **GID** - The numeric group ID
- **user_list** - A list of the usernames that are members of this group, separated by commas