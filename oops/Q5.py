# Polymorphism => one thing many work

# Demoonstrate polymorphism by defining a 
# method fuel_type in both Car and Electric_car 
# classes, but with different behaviour


class Car:
    
    def __init__(self, brand , model):
        self.__brand = brand
        self.model = model

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def get_brand(self):
        return self.__brand
    
    def fuel_type(self):
        return "petrol or disel"


class Electric_car(Car):

    def __init__(self, brand , model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric chagre"


electric_car = Electric_car("Tesla","model s", "85KWh")
print(electric_car.fuel_type())

fuel_car = Car("Tata", "nano")
print(fuel_car.fuel_type())