# bg

***Syntax*** - bg [job_id...]

- Send the specified jobs to the background. A background job is executed simultaneously with fish, and does not have access to the keyboard. If no job is specified, the last job to be used is put in the background.
  - bg takes a “job ID” available from jobs, not a PID

## Examples

- Put Put the job with job id 0 in the background:
  - $ bg %0

- To start a new process in the background you can do:
  - $ long_running_command &
