# Top

Process viewer, find the CPU-intensive programs currently running. See ps for explanations of the field descriptors

|**Options**| **Description** |
|--|--|
| `top` | Provides cpu memory usage and process IDs |
|`-b`  | Run in batch mode; don't accept command-line input. Useful for sending output to another command or to a file. |
|`-c` |Show command line in display instead of just command name |
|`-d` |delay (Specify delay between refreshes) |
|`-i` | Suppress display of idle and zombie processes|
|`-n` |Update display num times, then exit |
|`-p` |*pid* (Monitor only processes with the specified process ID)|
| `-q` | Refresh without any delay (If user is privileged, run with highest priority) |
|`-s` |Secure mode. Disable some (dangerous) interactive commands |
|`-S` | Cumulative mode. Print total CPU time of each process, including dead child processes|
