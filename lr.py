import doctest

# TODO Написать 3 класса с документацией и аннотацией типов

class Cup():
    def __init__(self, colour: str, capacity: float, form=True):
        """
        :param colour: цвет кружки
        :param capacity: наполненность кружки
        :param form: целостность изделия

        Пример:
        >>> cup = Cup("green", 100, True)
        """
        if not isinstance(capacity, (int, float)):
            raise TypeError('Объём кружки должен быть типа int или float')
        if not capacity > 0:
            raise ValueError("Объём кружки должен быть больше 0")
        self.colour = colour
        self.capacity = capacity
        self.form = True

    def brush(self, colour):
        """
        Функция перекрашивает кружку

        Примеры:
        >>> cup = Cup("red", 100, True)
        >>> cup.brush("blue")
        """
        ...

    def broke(self):
        """
        Функция разбивает кружку и делает невозмоэным совершение действий на ней

        :return: Состояние кружки

        Примеры:
        >>> cup = Cup("res", 100, True)
        >>> cup.broke()
        """
        ...

    def fill(self, capacity: [int, float]):
        """

        :param capacity: объём заполняемой жидкости
        :return: скольок воды в кружке
        Примеры:
        >>> cup = Cup("red", 100)
        >>> cup.fill(150)
        """
        if not isinstance(capacity, (int, float)):
            raise TypeError('Объём кружки должен быть типа int или float')
        if not capacity > 0:
            raise ValueError("Объём кружки должен быть больше 0")
        ...

class Car():
    def __init__(self, year: int, mileage: int, colour: str ):
        """

        :param year: год производства
        :param mileage: пробег (пройденные километры)
        :param colour: цвет автомобиля
        Пример:
        >>> car = Car(2015, 21000, "Volvo") # иницциализация экземпляра класса
        """
        if not isinstance(year, int):
            raise TypeError("Значение года должно быть целм числом")
        if year < 1886:
            raise ValueError("Год создания не может быть раньеш 1886")
        self.year = year

        if not isinstance(mileage, int):
            raise TypeError("Пробег автомобиля должен быть типа int")
        if year < 0:
            raise ValueError("Пробег автомобиля не может быть меньше 0")
        self.mileage = mileage

    def check_mileage(self):
        """
        Функция проверяет, нужен ли технический осмотр автомобиля в зависимости от пробега

        :return: Нужен ли ТО

        Примеры:
        >>> car = Car(2011, 59000, "white")
        >>> car.check_mileage()
        """

    def guarantee(self):
        """
        Функция проверяет действует ли гарантия на автомобиль

        :return: Действует ли гарантия

         Примеры:
        >>> car = Car(2011, 59000, "grey")
        >>> car.guarantee()
        """

    def recolour(self, new_colour: str):
        """
        Функция задаёт новый цвет автомобиля

        :param new_colour: новый цвет
        :return: новый цвет машины

        Пример:
        >>> car = Car(2014, 25862, "blue")
        >>> car.recolour("purple")
        """

class City():
    def __init__(self, population: int, capital: bool, name: str):
        """
        :param population: население города
        :param capital: статус столицы
        :param name: имя

        Пример:
        >>> city = City(1525852, False, "Town") # инициализвция экземпляра класса
        """
        if not isinstance(population, int):
            raise TypeError("Население города должно быть типа int")
        if population <= 0:
            raise ValueError("Население должно быть не отрицательным числом")
        self.population = population

        if not isinstance(capital, bool):
            raise TypeError("Статус столицы определяется типом boolean: True - столица, False - не столица")
        self.capital = capital

    def increase_population(self, people):
        """
        Функция увеличиет население города

        :param people: количество новых людей
        :return: итоговое население города

        Пример:
        >>> city = City(485, True, "CITY")
        >>> city.increase_population(78)
        """
        if not isinstance(people, int):
            raise TypeError("Количество людей должно быть типа int")
        if people <= 0:
            raise ValueError("Количество людей должно быть не отрицательным числом")
        self.people = people

    def check_capital(self):
        """
        Функция проверяет статус столицы города

        :return: является ли город столицей

        Пример:
        >>> city = City(852852, False, "Yarn")
        >>> city.check_capital()
        """

    def change_name(self, new_name):
        """
        Функция меняет парамент name

        :param new_name: новое название города
        :return: новое название города

        Пример:
        >>> city = City(852741, False, "Notr Dam")
        >>> city.change_name("Syktyvkar")
        """

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
