# n = int(input())
# res = 0
# for i in range(1, n + 1):
#     res += i
# print(res)

# ////////////////////////
#
# Написать алгоритм поиска простых чисел (делятся только на себя и
# на 1) в диапазоне от 1 до N. В алгоритме будет использоваться
# вложенный for, что явно говорит о квадратичной сложности, на этом
# стоит акцентировать внимание
#
# n = int(input())
# res = []
# for x in range(1, n + 1):
#     count = 0
#     for y in range(2, x+1):
#         if x % y == 0:
#             count += 1
#     if count == 1:
#         res.append(x)
# print(res)

#
# k = int(input())
# n = int(input())
# count = []
# for x in range(1, n + 1):
#     count = 0
#     for y in range(2, x+1):
#         if x % y == 0:
#             count += 1
#     if count == 1:
#         res.append(x)
# print(res)

#/////////////////////////////////////////////

n, m = map(int, input().split())
a = [[j * i for j in range(1, m+1)] for i in range(1, n+1)]
for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()