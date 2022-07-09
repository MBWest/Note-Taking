# Linux - Crontab

- A file that contains the schedule of `cron jobs` to be run and at which time to run them
- A cron job is a specific set of instructions that outlines the day and time a command should execute
    - A crontab can have multiple cron jobs 
- Each user has their own crontab
    - Located at /var/spool/cron/<username>
    - The system crontab is located at /etc/crontab
- Each crontab is read by `crond`, the daemon that executes scheduled commands

---

> ## **crontab [-u user] file || crontab [-u user] [-l | -r | -e] [-i] [-s]**
- Maintain crontab files for individual users
- `-u` - name of the user whose crontab is to be tweaked
- `-l` - the current crontab will be displayed
- `-e` - edit the current crontab

```
[root@CentOS ~]# crontab -l 
* * * * * w > /dev/null

[root@CentOS ~]# crontab -l -u chewie

[root@CentOS ~]# crontab -e
crontab: no changes made to crontab

[root@CentOS ~]# crontab -e -u chewie
no crontab for chewie - using an empty one
crontab: installing new crontab
```

---

> ## **Crontab Syntax (https://crontab.guru/)**

- There are 5 time and date fields that handle when the command will execute, followed by the command itself
- A `*` in a field means all legal values for that column
- Each of the time-related fields can contain:
    - A star, which matches everything
    - A single integer, which matches exactly 
    - Two integers separated by a dash, matching a range of values
    - A range followed by a slash and a step value, e.g., 1-10/2
    - A comma-separated list of integers or ranges, matching any value




```
+---------- Minute            (range: 0-59)
| +-------- Hour              (range: 0-23)
| | +------ Day of the Month  (range: 1-31)
| | | +---- Month of the Year (range: 1-12)
| | | | +-- Day of the Week   (range: 0-7, 0 or 7 is Sunday, or use names)
| | | | |  
* * * * * command to be executed 
```



| **a**|**b**|**c**|**d**|**e**|
|:-:|:-:|:-:|:-:|:-:|
| `Minute`| `Hour`  | `Day`  | `Month`  | `Day (of week)`  |
|0-59 |0-23  |1-31 |1-12  |0-6  |

| **Intervals**   | **Value**   |
|:-------------:|-------------------|
| **Example** |
| `Asterisk(*)` | Any Value |
| `5,6` | List of values (5 and 6) |
| `1-4` | Range of values (1 to 4) |
| `*/5` | Step values (every 5) |

---

> ## **Examples**

```
Minute – Hour – Day of Month – Month of Year – Day of Week - Command
```

```
# Remove the contents of /tmp every sunday at midnight
0 0 * * 7 rm -rf /tmp/*

# Rotate logs every day at 6am
0 6 * * * logrotate 

# will run at 2:01am on April 3rd, 
# and at 2:01am on every Friday of April
1 2 3 4 5 easteregg.sh

## there are other options available to you for finer grained control of timing
# check disk space every 10 minutes 
*/10 * * * * check_disk_space.sh

# every month, defrag 
@monthly defrag_disk
```

---

> ### **Run a job at minute 30, every hour (everytime the clock shows x:30)**

    | 30|*  |*  |*  |*  |
    |:-:|:-:|:-:|:-:|:-:|
    | `Minute`| `Hour`  | `Day`  | `Month`  | `Day (of week)`  |
    |0-59 |0-23  |1-31 |1-12  |0-6  |

---

> ### **Run a job every day at midnight (when hour is 0 and minute is 0)**

    | 30|6  |*  |*  |*  |
    |:-:|:-:|:-:|:-:|:-:|
    | `Minute`| `Hour`  | `Day`  | `Month`  | `Day (of week)`  |
    |0-59 |0-23  |1-31 |1-12  |0-6  |

---

> ### **Run a job every monday at 6:30AM**

    | 30|6  |*  |*  |1  |
    |:-:|:-:|:-:|:-:|:-:|
    | `Minute`| `Hour`  | `Day`  | `Month`  | `Day (of week)`  |
    |0-59 |0-23  |1-31 |1-12  |0-6  |

---

> ### **Run a job every monday in April at 6:30AM**

    | 30|6  |*  |4  |1  |
    |:-:|:-:|:-:|:-:|:-:|
    | `Minute`| `Hour`  | `Day`  | `Month`  | `Day (of week)`  |
    |0-59 |0-23  |1-31 |1-12  |0-6  |

---

> ### **Run a job at midnight on the first of every month**

    | 0|0  |1  |*  |*  |
    |:-:|:-:|:-:|:-:|:-:|
    | `Minute`| `Hour`  | `Day`  | `Month`  | `Day (of week)`  |
    |0-59 |0-23  |1-31 |1-12  |0-6  |

---

> ### **Run a job at midnight every weekday (monday-friday)**

    | 0|0  |*  |*  |1-5  |
    |:-:|:-:|:-:|:-:|:-:|
    | `Minute`| `Hour`  | `Day`  | `Month`  | `Day (of week)`  |
    |0-59 | 0-23  | 1-31 | 1-12  |0-6  |

---

> ### **Run a job every 5 minutes**

    | */5 |*  |*  |*  |*  |
    |:-:|:-:|:-:|:-:|:-:|
    | `Minute`| `Hour`  | `Day`  | `Month`  | `Day (of week)`  |
    |0-59 |0-23  |1-31 |1-12  |0-6  |