# bg

- Send the specified jobs to the background. A background job is executed simultaneously with fish, and does not have access to the keyboard. If no job is specified, the last job to be used is put in the background.
  - bg takes a “job ID” available from jobs, not a PID

> ## **Syntax** 


- bg [job_id...]

---

> ## **Example** 

| **Command**   | **Description**   |
| --------------|-------------------|
| `$ bg %0` | Put the job with job id 0 in the background. |
| `$ long_running_command &` | To start a new process in the background |
