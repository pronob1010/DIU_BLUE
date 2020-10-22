# https://acm.timus.ru/problem.aspx?num=1086

n=[]
def prime_eratosthenes(n):
    prime_list = []
    list = []
    for i in range(2, n+1):
        if i not in prime_list:
            list.append(i)
            for j in range(i*i, n+1, i):
                prime_list.append(j)

    return list
n = prime_eratosthenes(15000)

for k in range(int(input())):
    p = int(input())
    print(n[p-1])
