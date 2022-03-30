# Write a function, persistence, that takes in a positive parameter num and
# returns its multiplicative persistence, which is the number of times you must
# multiply the digits in num until you reach a single digit.


def persistence(num):
    # your code
    if num < 10:
        return 0  # Only one digit. Can't iterate over it
    num_str = str(num)
    total = 1
    for i in num_str:
        total = total * int(i)
    return 1 + persistence(total)




# For example:

print(persistence(39))
# returns 3, because 3*9=27, 2*7=14, 1*4=4
# and 4 has only one digit

print(persistence(999))
# returns 4, because 9*9*9=729, 7*2*9=126,
# 1*2*6=12, and finally 1*2=2

print(persistence(4))
# returns 0, because 4 is already a one-digit number


# Other way using counter ---------------------------------------------------
# The counter keeps track of how many times the loop runs, which gives you your final answer.
def persistance(num):
    counter=0
    while num>9:
        counter+=1
        num_str=str(num)
        total=1
        for i in num_str:
            total=total* int(i)
        num=total
    print (counter)

# Top way on CodeWars ---------------------------------------------------

import operator
def persistence(n):
    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i
