# Kill

## Most Common 

| **Signal** | **Description** |
|------------|-----------------|
|`1` |	SIGHUP - This is sent to a process when the terminal that controls it is closed. |
|`2` |	SIGINT - Sent when a user presses [Ctrl] + C in the controlling terminal to interrupt a process. |
|`3` |	SIGQUIT - Sent when a user presses [Ctrl] + D to quit. |
|`9` |	SIGKILL - Immediately kill a process with no clean-up operations. |
|`15` |	SIGTERM - Program termination. |
|`19` |	SIGSTOP - Stop the program. It cannot be handled anymore. |
|`20` | SIGTSTP - Sent when a user presses [Ctrl] + Z to request for a service to suspend. The user can handle it afterward. |