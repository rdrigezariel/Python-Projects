from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, capacity):
        self.capacity = capacity
        
    def maxCapacity(self):
        print("Your vehicle's max capacity is: ", self.capacity)

    @abstractmethod
    def load(self, capacity, passengers):
        pass

class Car(Vehicle):
    # here we have defined how to implement the load method from the Vehicle class.
    def load(self, passengers):
        if passengers > self.capacity:
            print('This car is not capable of handling {} passengers'.format(passengers))
        else:
            print('This car is capable of handling {} passengers'.format(passengers))

camry = Car(4)
camry.maxCapacity()
camry.load(5)

        
        
