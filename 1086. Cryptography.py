# https://acm.timus.ru/problem.aspx?num=1086

for i in range(int(input())):
    rangenumber=int(input())
    c = 0
    num = 2
    letest = 0

    while (c != rangenumber):
       count = 0
       for i in range(2,num):
          if (num % i == 0):
             count+=1
             break
       if (count == 0):
          c+=1
          letest = num
       num = num + 1
    print (letest)


#
# import math
#
# num = 11
#
# def prime(num):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 return False
#                 break
#         else:
#             return True
#     else:
#         return False
# for k in range(int(input())):
#     n = int(input())
#     i = 1
#     c = 1
#     while True:
#         if prime(i) is True:
#             if c<n:
#                 c+=1
#             else:
#                 print(i)
#                 break
#         i+=1
