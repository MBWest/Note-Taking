# # Conversions - Unsigned Binary (Base 2) to Hexadecimal (Base 16)

> ## **Example Problem**
>> ### **Convert 1010 from Binary to Hexadecimal**

```
1010
```
-  Binary numbers can only be 1 and 0. Hexadecimal numbers can be 0-9, or A-F, since hexadecimal is base-16. You can convert any binary string to hexadecimal (1, 01, 101101, etc.), but you need four numbers to make the conversion (0101→5; 1100→C, etc.).

---

> ### **2. Write the digits of the binary number below their corresponding powers of two.**

```
  1  |  0  |  1  |  0
 2^3 | 2^2 | 2^1 | 2^0 
 8   | 4   | 2   | 1
```

---

> ### **3. Connect the digits in the binary number with their corresponding powers of two.**

```
  1  |  0  |  1  |  0
  |           |
  8  | 4   |  2  |  1
```

---

> ### **4. Write down the final value of each power of two.**

```
  1  |  0  |  1  |  0
  |           |
  8  +  0  +  2  +  0
```

---

> ### **5. Add the final values.**

```

  1  |  0  |  1  |  0
  |           |
  8  +  0  +  2  +  0 = 10
```

---

> ### **6. Find the Value on the chart below.**

```
1010 = 10 = A
```

| **Binary (Base 2)**  | **Hexadecimal (Base 16)** |
|:-----------:|:---------------:|  
| `0` | 0 |
| `1` | 1 |
| `10` | 2 |
| `11` | 3 |
| `100` | 4 |
| `101` | 5 |
| `110` | 6 |
| `111` | 7 |
| `1000` | 8 |
| `1001` | 9 |
| `1010` | A (10) |
| `1011` | B (11) |
| `1100` | C (12) |
| `1101` | D (13) |
| `1110` | E (14) |
| `1111` | F (15) |