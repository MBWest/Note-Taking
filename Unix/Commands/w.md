# w

Show who is logged on and what they are doing

## Format

w
## Header Information

- The header shows, in this order, the current time, how long the system has been running, how many users are currently logged on, and the system load averages for the past 1, 5, and 15 minutes.
- Login name, the tty name, the remote host, login time, idle time, JCPU, PCPU, and the command line of their current process
- The JCPU time is the time used by all processes attached to the tty. It does not include past background jobs, but does include currently running background jobs
- The PCPU time is the time used by the current process, named in the "what" field

## Examples

- **w** - Displays information about the users currently on the machine, and their processes

## Options

- **-h** - Don't print the header
- **-u** - Ignores the username while figuring out the current process and cpu times. To demonstrate this, do a "su" and do a "w" and a "w -u"
- **-s**- Use the short format. Don't print the login time, JCPU or PCPU times
- **-f**- Toggle printing the from (remote hostname) field. The default as released is for the from field to not be printed, although your system administrator or distribution maintainer may have compiled a version in which the from field is shown by default
- **-V**- Display version information