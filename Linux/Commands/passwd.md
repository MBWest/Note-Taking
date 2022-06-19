# passwd

- Change user password
- A normal user may only change the password for their own account, while the superuser may change the password for any account.  passwd also changes the account or associated password validity period.

## Format

`passwd [options] [LOGIN]`

## Examples

| **Command**   | **Description**   | 
| --------------|-------------------|
| **Examples** |
| `passwd` | Prompts the user to enter a new password. This will change the current users password |
| `sudo passwd sally` | Promts the user to enter a new Password. This will change sally's passwod |

## Files

| **File**   | **Description**   | 
| --------------|-------------------|
| `/etc/passwd` | User account information. |
| `/etc/shadow` | Secure user account information. |
| `/etc/pam.d/passwd` | PAM configuration for passwd. |

## Exit Values

**The passwd command exits with the following values:**

| **Exit Value**   | **Description**   | 
| --------------|-------------------|
| `0` | Success |
| `1` | Permission denied |
| `2` | Invalid combination of options |
| `3` | Unexpected failure, nothing done |
| `4` | Unexpected failure, passwd file missing |
| `5` | Passwd file busy, try again |
| `6` | Invalid argument to option |