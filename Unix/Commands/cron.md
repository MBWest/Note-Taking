# Cron

The cron service allows you to schedule commands to run at regular intervals

## Editing the crontab

To set up a cron job, we need to edit the crontab configuration file. Rather than edit the files directly it is best to use the **crontab -e** command.

## Cron Syntax (https://crontab.guru/)

| a|b  |c  |d  |e  |
|--|--|--|--|--|--|
| Minute| Hour  | Day  | Month  | Day (of week)  |
|0-59 |0-23  |1-31 |1-12  |0-6  |

- asteric(*) - Any Value
- 5,6 - List of values (5 and 6)
- 1-4 - Range of values (1 to 4)
- */5 - Step values (every 5)

## Examples

1. Run a job at minute 30, every hour (everytime the clock shows x:30)
| 30|*  |*  |*  |*  |
|--|--|--|--|--|--|
| Minute| Hour  | Day  | Month  | Day (of week)  |
|0-59 |0-23  |1-31 |1-12  |0-6  |

2. Run a job every day at midnight (when hour is 0 and minute is 0)

| 30|6  |*  |*  |*  |
|--|--|--|--|--|--|
| Minute| Hour  | Day  | Month  | Day (of week)  |
|0-59 |0-23  |1-31 |1-12  |0-6  |

3. Run a job every monday at 6:30AM

| 30|6  |*  |*  |1  |
|--|--|--|--|--|--|
| Minute| Hour  | Day  | Month  | Day (of week)  |
|0-59 |0-23  |1-31 |1-12  |0-6  |

4. Run a job every monday in April at 6:30AM

| 30|6  |*  |4  |1  |
|--|--|--|--|--|--|
| Minute| Hour  | Day  | Month  | Day (of week)  |
|0-59 |0-23  |1-31 |1-12  |0-6  |

5. Run a job at midnight on the first of every month

| 0|0  |1  |*  |*  |
|--|--|--|--|--|--|
| Minute| Hour  | Day  | Month  | Day (of week)  |
|0-59 |0-23  |1-31 |1-12  |0-6  |

6. Run a job at midnight every weekday (monday-friday)

| 0|0  |*  |*  |1-5  |
|--|--|--|--|--|--|
| Minute| Hour  | Day  | Month  | Day (of week)  |
|0-59 |0-23  |1-31 |1-12  |0-6  |

7. Run a job every 5 minutes

| */5 |*  |*  |*  |*  |
|--|--|--|--|--|--|
| Minute| Hour  | Day  | Month  | Day (of week)  |
|0-59 |0-23  |1-31 |1-12  |0-6  |