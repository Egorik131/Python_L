class Car:
    pass

    def __init__(self, name: str, color: str, year: int):
        self.name = name
        self.color = color
        self.year = year
        self.spoiler = None //

    def __str__(self):
        return f'авто {self.name}, цвет {self.color} и {self.year} год выпуска'

    def horn(self):
        print('би би')


a = Car('M', 'b', 2003)
b = Car('T', 'g', 2010)

a.spoiler = 'Big and Black'
print(a.spoiler)
print(b.spoiler)

Книги.
https://t.me/dirty_python/221

print(a)
print(b)
print(a.name)
print(a.color)
print(a.year)
print(b.name)
print(b.color)
print(b.year)

a.horn()
b.horn()
