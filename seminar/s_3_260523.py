# collections

# List, список
# first_list = [9, 'fkr', True, [1, 2, 3]]

# for i, element in enumerate(first_list):
#     if element == 9:
#         first_list[i] = 'nine'
# print(first_list)

# print(first_list.remove(9))
# print(first_list)

# Стек в Python — это линейная структура данных
# «последним вошел — первым ушел»,
# т.е. элемент, введенный последним,
# будет первым удаляемым элементом.
# Операции, связанные со стеком: Push — Добавление
# элементов в стек. Pop — Удаление / удаление элементов из стека.

# first_list2 = [9, 10, 11, 3]
# print(first_list2)
# print(first_list2.sort())  # сортирует и ничего не возвращает
# # перезаписывает существующую коллекцию
# print(first_list2)
#
# print()
#
# # sorted(first_list2) #сортирует и не сохраняет (только возвращает)
# # создает новю коллекцию
# first_list3 = [9, 10, 11, 3]
# print(first_list3)
# print(sorted(first_list3))
# first_list4 = sorted(first_list3)
# print(first_list4)
# print(first_list3)
# разобраться сорт и сортед


# множестов
# first_set = set([1, 2, 3, 4, 5])
# second_set = set([2, 2, 6, 4, 5])
# # print(first_set.pop())
# print(second_set.issubset(first_set))
# print(first_set)

# Пересечение моножеств / пересечение
# differance


# картеж tuple
# first_tuple = (1, 'xxx', True)


# tuple - пароли, данные должны быть незимененными, ключи, и т.д.
# во всех осоальных случаях list
# set - для удаления дубликатов из списков
# a = [1,1,1,1,1,2,2,2,2,3,3,0,0,3]
# print(list(set(a)))


# Словарь
# first_dict = {'mom': 232323232, 'dad': 456456, 'frend': 789789}
#
# print(first_dict.pop('mom'))
# print(first_dict)
# second_dict = first_dict.copy()
# print(second_dict)

# Ключ неизменяемый тип данных

# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Задачи
# По примеру преподавателя)


# a = [1, 1, 2, 0, -1, 3, 4, 4]
# b = list(set(a))
# print(len(b))


# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
#
# while k < 3
# pop - удаляем
# insert - вставляем
#
# Срезы - как
#
# print("Enter num")
# num=int(input())
# arr.clear()
# for i in range(num):
#     arr.append(rand.randint(0,10))
#
# print("Enter k")
# k=int(input())
# print(arr)
# arr2=arr[:len(arr)-k]
# arr3=arr[len(arr)-k:]
# arr3.append(arr2)
# # print(arr3)
#  --------------------
#
# list_1 = []
# length = int(input('Enter length of list > '))
# k = int(input('k = '))
# for i in  range(length):
#     list_1.append(int(input()))
#
# print(list_1)
#
# for i in range(k):
#     tmp = list_1[-1]
#     list_1.insert(0, tmp)
#     list_1.pop()
#
# print(list_1)
#
#
# --------------------------------
#
# import random
# list_1 = list()
# for i in range(0, 10):
#     n = random.randint(0, 10)
#     list_1.append(n)
#
# print(list_1)
#
# step = int(input())
#
# result_list = list_1.copy()
#
# for i in range(step):
#     result_list.insert(0, result_list.pop())
# print(result_list)
#
# ---------------------------
#
# list = [1, 2, 3, 4, 5]
# k = int(input('k = '))
#
# for i in range(k - 1):
#     list.insert(0, list.pop())
# print(list)
#
# --------------------------------
#
# arr = [1, 2, 3, 4, 5]
# k = int(input())
# for i in range(k):
#     elem = arr.pop()
#     arr.insert(0, elem)
#
# print(arr)
#
# -------------------------

# list_1 = [1, 2, 3, 4, 5]
#
# print(list_1[3:]+list_1[:3])

# ------
# list.insert(0, list.pop()) - объясните пожалуйста эту строчку
# Инсерт вставляет в нулевую поизую лист pop который удаляется и сразу вставляется


# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# data = [
#     {"V": "S001"},
#     {"V": "S002"},
#     {"VI": "S001"},
#     {"VI": "S005"},
#     {"VII": "S005"},
#     {"V": "S009"},
#     {"VIII": "S007"}
# ]
#
# unique_values = set()
#
# for item in data:
#     for value in item.values():
#         unique_values.add(value.strip())  # Добавляем уникальные значения в множество
#
# print(list(unique_values))
#


# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

# list = [0, -1, 5, 2, 3]
# count = 0
# for i in range(len(list)-1):
#     if list[i] > list[i + 1]:
#         count += 1
#     print(count)
#
# list = [0, -1, 5, 2, 3]
# count = 0
# for i in range(1,len(a)):
#     if a[i-1] < a[i]:
#         count += 1
#     print(count)


# ----------------------------
# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

# метод count


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

# sort ... index ... index-+1

# Склаб


# Строку в список

# list превращает строку в список list(a)

# list comprehension
a = [int(a) for a in input().split()]
print(a)
# print('hell nnn ddd fff'.split())

a=[int(a) for a in input().split() if int(a)>0]
print(a)