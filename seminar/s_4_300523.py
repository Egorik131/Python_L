# Срезы
# a = 'Hello World'
# b = [1, 2, 3, 4, 5, 6, 7]
# print(a[:6])
# print(b[::-1])
# c = list(a)
# print(c)

# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

# s = 'a a a b c a a d c d d'
# s = s.split()
# print(s)
# final_string = ''
# for i in range(len(s)):
#     if s[0:i].count(s[i]) == 0:
#         final_string += f' {s[i]}'
#     else:
#         final_string += f' {s[i]}_{s[0:i].count(s[i])}'
# print(final_string)


# string = 'a a a b c a a d d d'
# elements = {}
# mess = ""
# for element in string.split():
#     if element not in elements:
#         elements[element] = 1
#         mess += f"{element} "
#     else:
#         elements[element] += 1
#         mess += f"{element}_{elements[element]-1} "
# print(mess)

# s = 'a a a b c a a d d d'
# st = list(s)
# print(st)
# d = {}
# p = ""
# for i in range(len(st)):
#     if d.get(st[i]) != None:
#         d[st[i]] = int(d[st[i]])+1
#     else:
#         d[st[i]] = 1
#     p = p + f"{st[i]}_{d[st[i]]}"
# print(p)

# print('aBcdEfg.?,!'.strip('.?,!\n').lower())


# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13
#
# text = '''She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure. So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells'''
#
# text = text.strip('.?,!\n').replace('.', ' ').lower().split()
# # text = text.strip('.?,!\n').lower().split()
#
# # text = text.split()
# print(text)
# print(set(text))
# text = list(set(text))
#
# print(f'Количество различных слов в тексте: {len(text)}')
#



# Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность).

n = int(input())
max_num = 0
while n > 0:
    n = int(input())
    if max_num < n:
        max_num = n
print(max_num)


