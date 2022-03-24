# yum

`Redhats` packet managing tool

## Format

dnf [options] <command> [<args>...]

## Examples

- **yum update** - Updates and upgrades the packages on the system
    - Requires `sudo`
- **yum search qpdf** - Searches for the qpdf in the repositories
- **yum info qpdf** - Provides a brief description of the requested application
- **yum install qpdf** - Installs the qpdf application
    - Requires `sudo`
- **yum remove qpdf** - Uninstalls the qpdf application
    - Requires `sudo`

## Resources

**RedHat documentation on managing software packages:** https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_basic_system_settings/managing-software-packages_configuring-basic-system-settings
