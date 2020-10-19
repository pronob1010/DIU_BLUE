# https://acm.timus.ru/problem.aspx?num=1068

n = int(input())
r=0
if n>0:
    for i in range(1,n+1):
        r+=i
    print(r)
elif n<0:
    for i in range(n,-1):
        r += i
    print(r)
else:
    print("1")