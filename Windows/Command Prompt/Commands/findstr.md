# findstr

| **Command** | **Description** |
|-------------|-----------------|
| `findstr /r "^07/[0-9]/2017" C:\uberdirlisting.txt` | Search C:\uberdirlisting.txt for anything with the date from 07/10/2017 to 07/19/2017 |
| `findstr /r "^07/[0-9]/2017.*\.txt$" C:\uberdirlisting.txt` | Now narrow that search to show only the files with the .txt extension |
| `findstr /r "^07/1[0-9]/2017.*\.jpg$ ^07/0[3-9]/2017.*\.jpg$" C:\uberdirlisting.txt` | Expand the date of that search 07/03/2017 to 07/19/2017 and show only the .jpg files.  |