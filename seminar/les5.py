# x = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()
# for i in x:
#     if i % 2 == 0:
#         res.append((i, i**2))
# print (res)

# def select(f, col):
#     return [f(x) for x in col]
#
#
# def where(f, col):
#     return [x for x in col if f(x)]
#
#
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x ** 2), res))
# print(res)
# //////////////////////////
# вариант с map

# def where(f, col):
#     return [x for x in col if f(x)]
#
#
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)


# //////////////////////////////////

# list_1 = [x for x in range(1, 20)]
# print(list_1)
#
# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)


# /////////////////////////////
# data = '12 15 12 34 56 1 2 3'
# # print(data)
# #
# # data = data.split()
# # print(data)
#
# data = list(map(int, data.split()))
# print(data)


# /////////////////////////////////////////
# filer

# data = [15, 69, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)

# //////////////////////////
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data)
# print(res)
# res = filter(lambda x: x % 2 == 0, res)
# print(res)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)

# ////////////////////////////
# zip