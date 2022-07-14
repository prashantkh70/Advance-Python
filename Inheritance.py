## Inheritance
## car class blueprint

class Car:
    def __init__(self, windows, doors, enginetype):
        self.windows = windows
        self.doors= doors
        self.enginetype=enginetype

    def driving(self):
        print("Car is used for driving")


#AUDI CAR IS INHERTING FROM CAR CLASS
class Audi(Car):
    def __init__(self, windows, doors, enginetype , horsepower):
        super().__init__(windows,doors,enginetype)
        self.horsepower = horsepower

    def selfdriving(self):
        print("It is a self driving car")

AudiQ7=Audi(4,5,"Diesel",200)

print(AudiQ7.horsepower)
print(AudiQ7.windows)
AudiQ7.driving()
AudiQ7.selfdriving()

car1= Car(2,4,"Diesel")
print(car1)
print(AudiQ7)

print(dir(AudiQ7))
print(dir(car1))