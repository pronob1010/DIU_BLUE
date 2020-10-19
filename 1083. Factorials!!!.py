# https://acm.timus.ru/problem.aspx?num=1083

a,b=list(map(str,input().split()))
n =int(a)
le =len(b)
r =1
for i in range(n,1,-le):
    r*=i
print(r)