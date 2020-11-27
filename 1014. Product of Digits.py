import math
n = int(input())
if n%2==0:
    print(n//2,end="")
    print(2)
elif math.sqrt(n)*math.sqrt(n)==n:
    print(int(math.sqrt(n)), end="")
    print(int(math.sqrt(n)))
else:
    print(-1)