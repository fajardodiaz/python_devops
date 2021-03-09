class Car:
    """A Simple Car Class"""
    def __init__(self,make,model,year):
        self.make = make
        self. model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"Car: {self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it!")

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back and odometer!")

    def increment_odometer(self,miles):
        self.odometer_reading =+ miles

class ElectricCar(Car):
    """Represent aspects for a car"""
    def __init__(self,make,model,year):
        super().__init__(make,model,year)


my_car = Car("audi","r8",2021)
print(my_car.get_descriptive_name())
my_car.increment_odometer(500)
my_car.read_odometer()

my_electric_car = ElectricCar("tesla","s",2020)
print(my_electric_car.get_descriptive_name())