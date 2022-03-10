# Subnetting

## Resources for this video:

Seven Second Subnetting: https://www.youtube.com/watch?v=ZxAwQB8TZsM

Subnet Guide: https://drive.google.com/file/d/1ETKH31-E7G-7ntEOlWGZcDZWuukmeHFe/view

## Hosts

- The number of bits switched off (0) is the number of hosts available.` 2^(number of 0's)`

## CIDR Notation

- The number of bits switched on (1).
    - *Example*> /24

## Subnetting Cheat Sheet

|Subnet x.0.0.0 |||||||||
|--|--|--|--|--|--|--|--|--|
|CIDR |/1|/2|/3|/4|/5|/6|/7|/8|
|Hosts |2,147,483,648|1,073,741,824|536,870,912|268,435,456|134,217,728|67,108,864|33,554,432|16,777,216|
|Class A |255.x.0.0||||||||
|CIDR |/9|/10|/11|/12|/13|/14|/15|/16|
|Hosts |8,388,608|4,194,304|2,097,152|1,048,576|524,288|262,144|131,072|65,536|
|Class B |255.255.x.0||||||||
|CIDR |/17|/18|/19|/20|/21|/22|/23|/24|  
|Hosts |32,768|16,384|8,192|4,096|2,048|1,024|512|256|  
|Class C |255.255.255.x||||||||
|CIDR |/25|/26|/27|/28|/29|/30|/31|/32|  
|Hosts |128|64|32|16|8|4|2|1|  
