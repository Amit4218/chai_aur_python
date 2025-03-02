# Static Method => is a method that belongs to a class rather than an instance of a class

# Add a static method to the Car class 
# that returns a general description of a car

# @staticmethod => are called decoraters in py. this one used to make a function static in a class

class Car:

    total_car_created = 0
    
    def __init__(self, brand , model):
        self.__brand = brand
        self.model = model
        self.total_car_created += 1 

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def get_brand(self):
        return self.__brand
    
    def fuel_type(self):
        return "petrol or disel"
    
    @staticmethod
    def general_description():
        return "car are a means of trasport on the land"


class Electric_car(Car):

    def __init__(self, brand , model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric chagre"
    

print(Car.general_description())