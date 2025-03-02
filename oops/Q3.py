# Inheritance
# Create a ElecricCar class that inherits from the 
# Car class and has an additional attribute battery_size

# super => something that is in its upper class

class Car:
    
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"


class Electric_car(Car):

    def __init__(self, brand , model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


tesla = Electric_car("Tesla", "Model S", "85KWh")
print(tesla.full_name())
