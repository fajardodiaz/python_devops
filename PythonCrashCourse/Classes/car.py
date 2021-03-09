class Car:
    """A Simple Car Class"""
    def __init__(self,make,model,year,odometer_reading):
        self.make = make
        self. model = model
        self.year = year
        self.odometer_reading = 0 

    def get_descriptive_name(self):
        long_name = f"Car: {self.year} {self.make} {self.model}"
        return long_name.title()

my_car = Car("audi","r8",2021)
print(my_car.get_descriptive_name())