class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)
    def __del__(self):
        return print(f'{self.name} снесён, но он останется в истории')
    def __init__(self, name, nof):
        self.name = name
        self.number_of_floors = nof
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
           return self.number_of_floors == other

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            return self.number_of_floors < other

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __gt__(self, other):
        return not self.__le__(other)
    def __ge__(self, other):
        return not self.__lt__(other)
    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            return self.number_of_floors != other
    def __add__(self, value):
        self.number_of_floors = self.number_of_floors + value
        return self
    def __radd__(self, value):
        self.number_of_floors = self.number_of_floors + value
        return self

    def __iadd__(self, other):
        self.number_of_floors = self.number_of_floors + value
        return self

    def go_to(self, new_floor):
        if self.number_of_floors < new_floor or self.number_of_floors < 1 :
            print('Такого этажа не существует')
        else:
            if new_floor <= 0:
                print('Такого этажа не существует')
            else:
                for i in range(1,new_floor + 1 ):
                    print(i)




h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)
