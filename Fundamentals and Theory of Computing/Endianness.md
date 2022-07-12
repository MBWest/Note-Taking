# Endianess


- Computers only understand binary. This means that `0`'s and `1`'s make up the language computers work with.
- One bit is one `0` or `1`. 8 bits make up a byte. 

---

> ## **What is Endianness**

- Endianness is a fundamental part of how computers read and understand bytes.
- Endianness means that the bytes in computer memory are read in a certain order.

---

> ## **Endianness is represented two ways Big-endian (BE) and Little-endian (LE)**

- `BE` stores the `big-end` first. When reading multiple bytes the first byte (or the lowest memory address) is the biggest - so it makes the most sense to people who read `left to right`.
- `LE` stores the `little-end` first. When reading multiple bytes the first byte (or the lowest memory address) is the littlest -  so it makes most sense to people who read `right to left`.

---

> ## **Example of How Endianness Works**

- **Decimal Number** - 9,499,938

The 0b at the beginning is just notation to let readers know it's binary.

- **Big-endian Binary** - 0b10010000|11110101|00100010

- **Little-endian Binary** - 0b00100010|11110101|10010000

---

> ## **Most Significant Byte (MSbyte)**

- We refer to the `byte` holding the `smallest position` as the `Least Significant Byte (LSbyte)` and the `bit` holding the `smallest position` as the `Least Significant Bit (LSbit)`.

- A diagram to illustrate that the byte containing the lowest position numbers is the least significant byte is seen below:

```Text
Decimal Number
65,535

Binary
0b1111111111111111

Byte Position
0b| 11111111 | 11111111
 MSbyte^     LSbyte^
 ```

- The `byte` that holds the `most significant position` is referred to as the `Most Significant Byte (MSbyte)` and the `bit` holding the `most significant bit position` is the `Most Significant Bit (MSbit)`.

Now knowing this new definition, we can define `BE` and `LE` as:

- Big endian stores data `MSbyte` first
- Little endian stores data `MSbyte` last


---

> ## **Why is this even an issue in the first place?**

- `BE` is the dominant order in any network protocols, and is referred to as `network order`, for example. 
- On the other hand, most PC's are `little-endian`.

---
---
> # **Resources**
>> ## **Endianness Explained With an Egg - Computerphile**
- https://www.youtube.com/watch?v=NcaiHcBvDR4