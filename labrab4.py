if __name__ == "__main__":
    # Write your solution here
    """Базовый класс Спорт"""
    class Sport:
        def __init__(self, name: str, duration: float = 10):
            """
            :param name:  название спорта
            :param duration: длительность спорта

            Пример:
        >>> sport = Sport("Бег", 5)
            """

            self._name = name
            self._duration = duration
            print("You create a sport!")

        @property
        def name(self):
            return self._name

        @property
        def duration(self) -> float:
            return self.duration

        @duration.setter
        def duration(self, new_duration):
            if not isinstance(new_duration, float):
                raise TypeError("Длительность должна быть типа float")
            if new_duration <= 0:
                raise ValueError("Длительность не может быть меньше 0")
            self._duration = new_duration

        def __str__(self):
            return f"Sport {self.name}, duration {self.duration}"

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r})"

        def do_sport(self, odd_time: float):
            """
            Функция запускаеь спорт

            :param odd_time: дополнительное время для занятия спортом

            Примеры:
            >>> sport = Sport("Бег", 5)
            >>> sport.do_sport(10)
            """
            spent_time = self.duration + odd_time
            print(f'Sport duration:{spent_time}')


    class BallSport(Sport):
        def __init__(self, name: str,duration: float = 10, number_of_people: int = 2):
            """
            :param name:  название спорта с мячом
            :param duration: длительность спорта с мячо
            :param number_of_people: клдичество человек для игры в этот спорт

            Пример:
            >>> sport = BallSport("Волейбол", 10, 12)
            """
            super().__init__(name, duration)
            self._number_of_people = number_of_people
            print("You create a sport with a ball!")

        @property
        def number_of_people(self):
            return self._number_of_people

        @number_of_people.setter
        def number_of_people(self, new_number_of_people):
            if not isinstance(new_number_of_people, int):
                raise TypeError("Количество человек должно быть типа int")
            if new_number_of_people <= 0:
                raise ValueError("Количество человек не может быть меньше 0")
            self._number_of_people = new_number_of_people

        def __str__(self):
            return f"Sport {self.name} for {self.number_of_people} people, duration {self.duration}"

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, number_of_people={self.number_of_people!r}, duration {self.duration})"

        def do_sport(self, odd_time: float = 5):
            """
            Функция запускаеь спорт. Длительность игры зависет от количества человек

            :param odd_time: дополнительное время для занятия спортом

            Примеры:
            >>> sport = Sport("Бег", 5)
            >>> sport.do_sport(10)
            """
            spent_time = self.number_of_people * 0.5 + self.duration + odd_time
            print(f"You plat {self.name} for {spent_time} minutes")
    pass
