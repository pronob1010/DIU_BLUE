# d = {0:'a',1:'b'}
# d2 = [1,2]
# # b=d.copy()
# # b[2]='D'
# # print(d)
# # for i in d.keys():
# #     print(d[i])
# for i in d2:
#     print(d2.add(i))
#     #
# print('adc' 'fdf')
# print(''.isdigit())
# d2 = [1,2,3,4]
# d2[1:2]=[7,8]
# print(d2)
# b=d2.copy()
# b.add(4)
# print(d2)
# def f(a):
#     a = a+'2'
#     a = a*2
# print([ind.lower() for ind in 'Hello'])
# x =2
# for i in x:
#     x-=2
#     print(x)
# #     print(d2.add(i))
#
# print('Ar Ddc'.istitle())
#a = {'B':5,'A':9,'C':7}
# sorted(a)
# print(a)
# a = 40
# b= 30
# a =a^b
# b=a^b
# a=a^b
# print(a,b)
# print('helo'.partition('lo'))
#
# for i in range(5):
#     if i == 3:
#         break
#     else:

# print("yz90".isalnum())
# a = 'hello'
# a2 = ','
# a3= 'world'
# print(a[-1:])

# if (9<0) and (0<-9):
#     print("fd")
# elif (9>0) or False:
#     print("fdfd")
# else:
#     print("dfd")
# z = set('abc')
# z.add('san')
# z.update(set(['p','q']))
# print(z)
#
# s = [1,2,3]
# s2 = {1,2,3}
# s.pop()
# s2.pop()
# print(s2)
# print(s)
#
# x=8
# print(x>>2)
# print(2+4.00, 2**4.0)
# s = (1,2,3)
# del s
# print(list(enumerate([2,3])))
# a = [[1,2,3],[4,5,6],[7,8,9]]
# print([a[i][i] for i in range(len(a))])
# t = (1,2,4,3)
# print(t[1:3])
# print('{:,}'.format(1112223334))
# print('abc XYZ'.capitalize())
# print('-om')
t = [13,56,17]
# t.append([87])
# t.extend([45,67])
# print(t)
# print(all([13,56,17]))
# x = 'hello'
# print(x[:2])
# i ='a'
# while i in x[:-1]:
#     print(i)
# x = 'hello'
# # print(x[:2])
# d = {1:'a',2:'b',3:'c'}
# print(d.get(1,4))
#
# a={}
# a['a']=1
# a['b']=[2,3,4]
# print(a)

# print(any([2>8,4>2, 1>2]))
# print(int('10.8'))
#
# def pf(m , t = 1):
#     print(m*t)
# pf('e')
#
# s = (2,3,4)
# print(sum(s,3))
# print(round((0.5)_round(-0.5)))

# print('xyyzxxyxyy'.lstrip('xyy'))
#
# float('56'+45?)

#!/bin/python3


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
line = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

for i in range(m):
    p = 1
    s = ''
    for j in range(n):
        if ((matrix[j][i]>='A' or matrix[j][i]>='a') and((matrix[j][i]<='z') or matrix[j][i]<='Z')):
            if p == 0:
                line.append(' ')
                s = ''
            line.append(matrix[j][i])
            p=1
        else:
            s+=matrix[j][i]
            p = 0


    line.append(s)

print(*line,sep="")