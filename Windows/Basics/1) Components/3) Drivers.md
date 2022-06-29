# Windows Drivers

> **Definition:** Software component that enables communication between hardware and the OS:
- Can communicate directly with the hardware
- Can communicate with lower-level drivers 
    - Ex: Graphics Cards

---
---
---

```Text
|-----------|       |-----------|       |-----------|       |-----------|
|           |-------|  Windows  |-------|  NVIDIA   |-------| Grpahics  |
|  Skyrim   |       |    OS     |       |  Driver   |       |   Card    |
|           |       |           |       |           |       |           |
|-----------|       |-----------|       |-----------|       |-----------|
```
---
---
---

## **Driver Modes**

> **User Mode**
- Interface between a Win32 application and kernel-mode drivers or other OS components (not actual hardware).

> **Kernel Mode**
- Interface with I/O, Plug and play memory, process and thread management, security, etc.

---
---
---

## **Driver Levels**

> **Highest-level**
- Always depend on `lower level` drivers for support
- Examples include file system drivers for: NTFS, FAT, CDFS
> **Intermediate-level**
- Always depend on `lower level` drivers for support
- Divided into: `Function, Filter, Software Bus Drivers`
> **Lowest-level**
- Control I/O bus in which the `actual hardware` device is connected
- Does `not` depend on lower-level drivers
- Example: AGP/PCI `hardware` bus drivers

---
---
---

## **Driver Levels - Intermediate-level**

> **Function Drivers**
- Handles reads/writes to the device
- Manages device power policy

> **Filter Drivers**
- Optional component, Provides additional functionality
- Communicates with other `filter` drivers or `function` drivers

> **Software Bus Drivers**
- Provides an interface for higher-level drivers to attach to a set of child devices

---
---
---

## **Driver Categories**

> **Software**
- Created to gain access to data accessible only to the kernel and is not associated with a hardware device
Always runs in `kernel` mode

> **Bus**
- Provides communication to the several devices sharing a bus
- Always runs in `kernel` mode
- Example - peripheral component interconnect (PCI) bus, USB bus

> **Device**
- Refers to drivers necessary for the OS to communicate with an attached device
- Can run in `User or Kernel` mode