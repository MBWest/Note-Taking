# tz

TZ Specifies the timezone, unless overridden by command line parameters. If neither is specified, the setting from /etc/localtime is used by Linux/UNIX computer.

# Examples 

- **TZ=America/Los_Angeles awk '/midnitemeerkats/ {print strftime("%T", $1), $3, $7}' access.log**
    - **TZ=America/Los_Angeles** - Temporarily sets the local timezone to America/Los_Angeles. This is needed because the timestamps are stored in the UTC timezone, and the strftime function can only display timestamps according to either UTC, or the local system timezone.
    - **strftime("%T", $1)** - print the timestamp in HH:MM:SS format.
