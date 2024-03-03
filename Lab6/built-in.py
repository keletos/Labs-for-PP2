from functools import reduce

def multiply(a):
    return reduce(lambda x,y : x*y, a)

#

s = input()

upper = sum(map(lambda x: x.isupper(), s))
lower = sum(map(lambda x: x.islower(), s))

print(upper, lower)

#

s = input()
print("YES") if s == s[::-1] else print("NO")

#

from time import sleep
from math import sqrt
x = int(input())
time = int(input())

def sqrtt(x, time):
    sleep(time//1000)
    print(f"Square root of {x} after {time} miliseconds is {sqrt(x)}")

sqrtt(x, time)

#

tupleBaha = (1,4, "s", [2])
print(all(tupleBaha))