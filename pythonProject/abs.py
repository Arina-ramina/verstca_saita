from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

class Car(Vehicle):
    def go(self):
        print('Машина едет')
class Motorcycle(Vehicle):
    def go(self):
        print('Мотоцикл едет')


car = Car()
motorcycle = Motorcycle()
print (car)
print(motorcycle)