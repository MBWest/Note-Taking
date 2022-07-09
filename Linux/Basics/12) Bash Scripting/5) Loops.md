# Linux - Bash Scripting - Loops

## **Syntax**

```bash
#!/bin/bash

for VARIABLE_NAME in ITEM_1 ITEM_N
do
    command 1
    command 2
    command N
done
```
## **Examples**

```bash
#!/bin/bash

for COLOR in red green blue
do
    echo "COLOR: $COLOR"
done
```

```bash
#!/bin/bash
COLORS="red green blue"

for COLOR in $COLORS
do
    echo "COLOR: $COLOR"
done

```
---
### **Take all .JPG pictures and rename them**

```bash
#!/bin/bash
PICTURES=$(ls *jpg)
DATE=$(date +%F)

for PICTURE in $PICTURES
do
    echo "Renaming ${PICTURE} to ${DATE}-${PICTURE}"
    mv ${PCITURE} ${DATE}-${PICTURE}
done
```
---

### **Looping through directory listing**

```bash
#!/bin/bash

for i in $( ls ); do
    echo item: $i
done
```

---

### **Loop through a file (dirs.txt) with a list of directories and copy**

```bash
#!/bin/bash

while read p; do
    echo $p
    cp PRODUCT_INFO.md $p
done < dirs.txt
```
---

### **Range**

```bash
#!/bin/bash

for i in {0..40}; do wget http://10.10.10.245/data/${i}; done
```
---

### **Infinite loop**

```bash
#!/bin/bash

while true; do nc -w0 -v 10.10.10.10 514 <<< "Hello There"; sleep 2; done
```