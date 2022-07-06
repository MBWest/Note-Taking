# Device Names

| **Device Name** | **Description** |
|-----------------|-----------------|
| `/dev/hd*` | The hd* stands for hard disk, but in this case only refers to Integrated Drive Electronics (IDE) devices--that is, common hard disks. The first letter after the hd dictates the physical disk drive: `-` /dev/hda3 First drive, or primary master `-` /dev/hdb3 Second drive, or primary slave `-` /dev/hdc2 Third drive, or secondary master `-` /dev/hdd2 Fourth drive, or secondary slave *Note: the number following the drive name indicates the partition, which acts as a disk giving the effect of having more than one disk on a physical drive. |
| `/dev/sd*` | The sd stands for SCSI disk, the high-end drives mostly used by servers. Probing goes by SCSI ID and has a system completely different from that of IDE devices. For example, sda is the first physical disk probed, and /dev/sda1 is the first partition on the first drive. |
| `/dev/ttyS*` | The ttyS* are serial devices numbered from 0 up. The /dev/ttyS0 is the first serial port (COM1 under MS-DOS or Windows). With a multiport card, these can go to 32, 64, and up. |
| `/dev/psaux` | The psaux equates to PS/2 mouse. |
| `/dev/mouse` | A mouse is a symlink to /dev/ttyS0 or /dev/psaux. Other mouse devices are also supported. |
| `/dev/modem ` | A modem is a symlink to /dev/ttyS1 or whatever port the modem is on. |
| `/dev/fd*` | The fd* stands for floppy disk; fd0 is equivalent to the A: drive and fd1 is equivalent to the B: drive. The fd0 and fd1 devices auto detect the format of the floppy disk, but can explicitly specify a higher density by using a device name like /dev/fd0H1920, which gives access to 1.88 MB, formatted, 3.5-inch floppies. *Note: there are other floppy devices (l, m, and nnnn) |
| `/dev/par*` | A par* equates to a parallel port and /dev/par0 is the first parallel port or LPT1 under DOS. |
| `/dev/random`| /dev/urandom The random and urandom are random byte generators. Reading from these device gives pseudo-random numbers; if available /dev/urandom is preferred for secure applications. |
| `/dev/st*` | The st* stands for SCSI tape and is a SCSI backup tape drive. |
| `/dev/zero` | A zero produces ASCII-zero bytes (as many as are needed) and is useful if a user needs to generate a block of zeros. |
| `/dev/null` | A null is used to discard output; it is often seen with redirection, when viewing output is not desired. |
| `/dev/sr*` | An sr* stands for the SCSI CD-ROM. |
| `/dev/scd*` | An scd* is an alternate name for the SCSI CD-ROM |
| `/dev/sg*` | The sg* Stands for SCSI generic and is a general-purpose SCSI command interface for devices like scanners. |
| `/dev/fb*` | The fb* stands for frame buffer and represents the kernel's attempt at a graphics driver. |
| `/dev/cdrom` `/dev/dvdrom` | The cdrom is a symlink to whichever device is the optical drive on the system. |
| `/dev/tty*` |  A tty* is a virtual console and is the terminal device for the virtual console itself. They are numbered; /dev/tty1 through /dev/tty6 are the most common. |