from __future__ import annotations


class Vehicle:
    definition = 'a mechanism that can move'
    def __init__(self,wheels: int | None):
        self.wheels = wheels


    def move(self):
        print(f'{self.__class__.__name__} is moving')

class Bysicle(Vehicle):
    pass

class Car(Vehicle):
    pass

class Train(Vehicle):
    definition = 'a mechanism that can move, but only within railroads '

class Helicopter(Vehicle):
    def move(self):
        print(f'{self.__class__.__name__} is flying fast')

    def move_parent(self):
        super().move()



v = Vehicle(None)
v.type = 'land'



bic = Bysicle(2)
trn = Train(12)
car = Car(4)
hel = Helicopter(0)

for v in (bic, car, trn, hel):
    print(f'{v.__class__.__name__} has {v.wheels} wheels')
    v.move()
hel.move_parent()

print(bic.definition)
print()
print(trn.definition)
