# Conversions - Unsigned Binary (Base 2) to Decimal (Base 10)

> ## **Example Problem**
>> ### **Convert 10011011 from Binary to Decimal**

```Binary
10011011
```
---

> ### **1. Write down the binary number and list the powers of 2 from right to left.**


```
2^7 | 2^6 | 2^5 | 2^4 | 2^3 | 2^2 | 2^1 | 2^0 
128 | 64  | 31  | 16  | 8   | 4   | 2   | 1
```

---

> ### **2. Write the digits of the binary number below their corresponding powers of two.**

```
 1  |  0  |  1  |  1  |  1  |  0  |  1  |  1
2^7 | 2^6 | 2^5 | 2^4 | 2^3 | 2^2 | 2^1 | 2^0 
128 | 64  | 31  | 16  | 8   | 4   | 2   | 1
```

---

> ### **3. Connect the digits in the binary number with their corresponding powers of two.**

```
 1  |  0  |  1  |  1  |  1  |  0  |  1  |  1
 |           |     |     |           |     |
128 | 64  |  31  | 16  | 8  |  4  |  2  |  1
```

---

> ### **4. Write down the final value of each power of two.**


```
 1    0    1    1    1    0    1    1
 |         |    |    |         |    |
128 + 0  + 31 + 16 + 8  + 0  + 2  + 1
```
---

> ### **5. Add the final values.**

```
 1    0    1    1    1    0    1    1
 |         |    |    |         |    |
128 + 0  + 31 + 16 + 8  + 0  + 2  + 1 = 155
```
---

> ### **6. Write the answer along with its base subscript.**

```

10011011 (Base2)
==
155 (Base10)