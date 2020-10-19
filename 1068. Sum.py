# https://acm.timus.ru/problem.aspx?num=1068

n = int(input())
nn = abs(n)
r = 0
for i in range(2,nn+1):

    r+=i
if n>0:
    print(r)
else:
    print("-",end="")
    print(r)
