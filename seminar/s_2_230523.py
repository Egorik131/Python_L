# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while

# n = int(input())
# res = 1
# while n > 0:
#     res *= n
#     n -= 1
# print(res)

# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# f0 = 0 f1 = 1 f2 = 1

# a = int(input())
# f1 = 0
# f2 = 1
# fib = 0
# count = 2
# while fib <= a:
#     fib = f1 + f2
#     f1 = f2
#     f2 = fib
#     count += 1
# if fib == a:
#     print(count)
# elif fib > a:
#     print(count - 1)
# else:
#     print(-1)

# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

# n = int(input())
# count = 0
# max1 = 0
# for i in range(n):
#     temp = int(input())
#     if temp > 0:
#         count += 1
#         if count > max1:
#             max1 = count
#     else:
#         count = 0
# print('count = ', max1)


# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

# n = int(input())
# min1 = int(input())
# max1 = min1
# for i in range(n-1):
#     temp = int(input())
#     if temp > max1:
#         max1 = temp
#     if temp < min1:
#         min1 = temp
# print(min1, max1)




