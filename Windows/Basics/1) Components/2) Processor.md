# Windows Processor

## **Runs in two modes:**

> ### **User Mode - Unprivileged/Restricted**
- Has its own private virtual address space in memory
- Isolates the app preventing alteration of:
    - Other application data
    - The OS itself

---

> ### **Kernel Mode - Privileged/Unrestricted**

- Everything shares the same virtual address space
- Possible to overwrite other programs and compromise the entire system (system crash)

---
---

```text
                                           |-----------|
                                           | User-Mode |
   User                                    |  Drivers  |
   Mode                                    |           |  
                                           |-----------|
                                                |
                                                |
                |-----------|              |-----------|
                | User-Mode |              |  Windows  |
                |  Drivers  |--------------|    API    |
                |           |              |           |
                |-----------|              |-----------|
_____________________|___________________________|_________________________________________________
                     |                           |
  Kernel        |-----------|           |---------------------|         |-----------|
  Mode          |   Other   |           |  Exported Drivers   |         |   File    |
                |Kernel-Mode|-----------|  Supported Routines |---------|  System   |
                |  Drivers  |           |  ----------------   |         |  Drivers  |
                |-----------|           |  |   OS Kernel  |   |         |-----------|
                     |    |             |  ----------------   |               |
                     |    |             |---------------------|               |
                     |    |                       |                           |
                     |    |----------------------------------------------------
                     |                            |
                     |                            |
                     |---------------------------------------------------------------|
                     |               Hardware Abstraction Layer                      |
                     |---------------------------------------------------------------|
                                                  |
                                                  |
                     |---------------------------------------------------------------|
                     |                         Hardware                              |
                     |---------------------------------------------------------------|
```