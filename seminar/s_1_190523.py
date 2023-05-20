 # Задача 1
# print('a', 'b','c', sep=' - ', end=' ')
# print(1, 2, 3, sep=' + ')

# name = input('Enter your name')
# print(f'name: {name}')

# a = [1, 2, 3, 4]
# for element in a:
#     print(element)
#
# a = [1, 2, 3, 4]
# for i in range (len(a)):
#     if a[i] > 2:
#         print(f'{i}-th elem >2')
#
# a = [1, 2, 3, 4]
# for i, element in enumerate(a):
#     if element > 2:
#         print(f'{i}-th element >2')
#
# n=10
# while n >= 1:
#     print(n)
#     n -= 1
#
#
#
#
# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n%i == 0:
#         flag = False
#         print(i)
#     elif i > n//2:
#         print(n)
#         flag = False
#     i +=1





# import math
# n = int(input('n = '))
# m = int(input('m = '))

# print(f'Количество дней в пути: {math.ceil(m / n)}')
# Еще вариант
# semi_res=m/n
# print(semi_res+(1-(semi_res%1)))

# # Задача 2
# k1 = int(input('Кол-во учеников в первом классе: '))
# k2 = int(input('Кол-во учеников во втором классе: '))
# k3 = int(input('Кол-во учеников в третьем классе: '))
# count = 0
# if k1 % 2 == 0:
#     count += k1 // 2
# else:
#     count += k1 // 2 + 1
# if k2 % 2 == 0:
#     count += k2 // 2
# else:
#     count += k2 // 2 + 1
# if k3 % 2 == 0:
#     count += k3 // 2
# else:
#     count += k3 // 2 + 1
# print(f'Наименьшее количество парт: {count}')
# print(int(k1/2+0.9)+int(k2/2+0.9)+int(k3/2+0.9))

# Задача 5 - Вагоны
# v1 = int(input('Номер вагона от головы поезда: '))
# v2 = int(input('Номер вагона: '))
# if v2 > v1:
#     print (f'В поезде {v2 + v1 - 1} вагона(ов)')
# else:
#     print('Без дополнительной информации это сделать невозможно')

# Задача 7 - Год
# y = int(input())
# if y % 4 == 0:
#     if y % 400 == 0:
#         print("Yes")
#     elif y % 100 == 0:
#         print("NO")
#     else:
#         print("YES")
# else:
#     print("NO")