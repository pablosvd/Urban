class House:
    def __init__(self, name, nof):
        self.name = name
        self.number_of_floors = nof
    def go_to(self, new_floor):
        if self.number_of_floors < new_floor or self.number_of_floors < 1 :
            print('Такого этажа не существует')
        else:
            if new_floor <= 0:
                print('Такого этажа не существует')
            else:
                for i in range(1,new_floor + 1 ):
                    print(i)

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
