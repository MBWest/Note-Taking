# schtasks

- Schedules commands and programs to run periodically or at a specific time, adds and removes tasks from the schedule, starts and stops tasks on demand, and displays and changes scheduled tasks.

---

> ## **Examples**


| **Command** | **Description** |
|-------------|-----------------|
| `schtasks /delete /tn Test`|  Deletes the schtask 'Test' |
| `schtasks /create /?` | Show a help page for creating a task (this applies for delete, query, etc.) 
| `schtasks /create /TN games /TR “C:\game.exe” /SC minute /MO 2` | Create a task Named “games” that will run “game. exe” scheduled for 2min intervals |
| `schtasks /query /TN games` | Query the pre-existing task name “games” |
| `schtasks /run /TN rubber-duck` | Run the scheduled task “rubber-duck” |
| `schtasks /change /disable /TN “games”` | Disabling the pre-existing task named “games” |
| `schtasks /delete /TN games` | Deleting the task using the task name “games” |