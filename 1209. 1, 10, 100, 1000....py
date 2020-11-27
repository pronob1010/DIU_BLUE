# https://acm.timus.ru/problem.aspx?num=1209
# import math
# for _ in range(int(input())):
#     n = int(input())
#     if int(math.sqrt(2*n-2))==int(math.sqrt((n*(n-1))))==int(n-1):
#         print(1)
#     else:
#         print(0)



# i = 1
# r = 1
# n = []
# while (i <= 20):
#     r += i - 1
#     n.append(r)
#     i+=1
# print(n)

# for _ in range(int(input())):
#     x = int(input())
#     if x in n:
#         print(1)
#     else:
#         print(0)

#
# for _ in range(int(input())):
#     n = int(input())
#
#     i = 1
#     r = 1
#     while (i <= n):
#         r += i - 1
#
#         # print(r)
#         if n == r:
#             print(1,end=" ")
#             break
#         i += 1
#     else:
#         print(0,end=" ")


import math
for _ in range(int(input())):
    n = int(input())

    c = int((math.sqrt(1+8*n)-1)/2)
    if n==1 or n-(c*(c+1))//2==1:
        print(1,end=" ")
    else:
        print(0,end=" ")

    # if n == r:
    #     print(1,end=" ")
    #     break
    #
    # else:
    #     print(0,end=" ")
