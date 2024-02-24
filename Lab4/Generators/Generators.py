n = int(input())
[print(i) for i in range(0,n+1) if i%2 == 0]

#

N = int(input())

def squares(n):
    return [i**2 for i in range(1,n+1)]

print(squares(N))

#

def Divided_By3and4(n):
    nums = [i for i in range(n+1) if i%3 == 0 and i%4 == 0]
    return nums

#

def nums(n):
    for i in range(n,-1, -1):
        yield i

nums = nums(int(input()))

for i in nums:
    print(i)

#

def squares(a,b):
    for i in range(a,b+1):
        yield i**2

nums = squares(int(input()), int(input()))
for i in nums:
    print(i)