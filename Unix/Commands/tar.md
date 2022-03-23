# Tar

An archiving utility

## Options

|Options| Description  |
|--|--|
| -c, --create | Create a new archive |
|-x, --extract | Ex |
|-t, --list | List the table of contents of an archive |
|-v, --verbose | Verbose, Shows which files get archived or extracted |
|-f, --files |File name. This option must be followed by the file name of the archive to use or create |
|-p, --preserve-permissions | Preserve the permissions of files and directories when extracting an archive, without subtracting the unmask |
|-z, --gzip | Use gzip compression (.tar, .gz) | 
| -j, --bzip2 | Use bzip2 compression (.tar, .bz2). Bzip2 typically achieves a better compression ratiio than gzip |
| -J, --xz | Use xz compression (.tar, .xz). The xz compression typically achieves a better compression ratio than bzip2 |

## Examples

- **tar cvf backup.tar file?.txt dir? shakespeare.txt**
    **tar** - The GNU version of the tar archiving utility
    **-c, --create**
      create a new archive
   **-v, --verbose**
      verbosely list files processed
    **-f, --file ARCHIVE**
      use archive file or device ARCHIVE
    tar [-] A --catenate --concatenate | c --create | d --diff --compare | --delete | r --append | t --list |
    --test-label | u --update | x --extract --get [options] [pathname ...]