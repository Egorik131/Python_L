class Car:
    car_type = 'Машина'

    def __init__(self, name: str, color: str, year: int):
        self.name = name
        self.color = color
        self.year = year
        self.spoiler = None

    def __str__(self):
        return f'Автомобиль {self.name}, цвета {self.color} и {self.year} года выпуска'