# Locate Command

- The locate command references a pre-generated database file rather than searching the entire matchine. Update this database using the **updatedb** command.
- The **locate** command performs a search of pathnames across the machine that match a given substring and then prints out any matching names
- *Example* > `locate chick`
	- Locates all files and directories with the name 'chick' in them

**You can use expansion characters (*, ?) to narrow down the search**
- *Example* >  `locate /bin/less???`
	- locates all files that contain the /bin/less with exactly 3 characters afterwards.