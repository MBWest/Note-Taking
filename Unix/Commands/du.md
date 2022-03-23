# du

- **du** - Allows a user to gain disk usage information quickly

        [tcarrigan@rhel article_submissions]$ du /home/tcarrigan/article_submissions/
        12    /home/tcarrigan/article_submissions/my_articles
        36    /home/tcarrigan/article_submissions/community_content
        48    /home/tcarrigan/article_submissions/

## Options

- **-h, --human-readable** - Prints size outputs in a human-readable format
- **-s, --summarize** - The -s flag is added to the -h flag on occasion. this allows the user to get a summary of the directoy's in a human-readable format

        [tcarrigan@rhel article_submissions]$ du -sh /home/tcarrigan/article_submissions/
        48K    /home/tcarrigan/article_submissions/

- **-a, -all** - Lists the sizes of all files and directories in the given file path. The -a is often combined with the -h flag for ease of use
- **--time** - Shows the time of the last modification to any file in the directory or subdirectory that you run it against
- **-c, --total** - Addes a line to the bottom of the output that gives you a grand total of all the disk usage for the file path given

        [tcarrigan@rhel article_submissions]$ du -ch /home/tcarrigan/article_submissions/
        12K    /home/tcarrigan/article_submissions/my_articles
        36K    /home/tcarrigan/article_submissions/community_content
        48K    /home/tcarrigan/article_submissions/
        48K    total
- **-X, --exclude=Pattern** - Excludes filetypes from your calculations