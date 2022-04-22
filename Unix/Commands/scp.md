# scp

OpenSSH secure file copy

## Examples

| **Command**   | **Description**   |
| --------------|-------------------|
| **Example** |
| `scp [SourcePath] [IP]:[DestinationPath]` | Copies files accross the network using the encrypted ssh protocol |
| `scp -r [SourcePath] [IP]:[DestinationPath]` | Copies a directory and all its content to a remote computer |
| `scp [IP]:[RemoteSourcePath] [DestinationPath]` | Copies files from the remote machine to a local machine|
| `scp -r [IP]:[RemoteSourcePath] [DestinationPath]` | Copies a directory and all its content from the remote machine to a local machine|
| `scp [SourcePath] [UserAccount]@[IP]:[DestinationPath]` | Copies files accross the network using the encrypted ssh protocol using a specific user account |
