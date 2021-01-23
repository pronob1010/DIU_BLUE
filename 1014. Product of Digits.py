import math
while True:
    n = int(input())
    x = int(math.sqrt(n))
    if n==1:
        print(-1)
    elif n%3==0:
        print(3, end="")
        print(n//3)
    elif n%2==0:
        f = 0
        if n//2<2:
            print(n//2, end="")
            f = 1
        else:
            print(2, end="")

        if f == 0:
            print(n//2)
        else:
            print(2)

    elif (x*x)==n:
        print(x, end="")
        print(x)
    else:
        print(-1)