# Multiple Inheritance

# Create two classe Battery and Engine, and let the Electric_car inherit from , demonstrating multiple inheritance


class Car:

    total_car_created = 0
    
    def __init__(self, brand , model):
        self.__brand = brand
        self.__model = model
        self.total_car_created += 1 

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def get_brand(self):
        return self.__brand
    
    def fuel_type(self):
        return "petrol or disel"
    
    @staticmethod
    def general_description():
        return "car are a means of trasport on the land"
    
    @property
    def model(self):
        return self.__model
    



class Electric_car(Car):

    def __init__(self, brand , model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric chagre"
    

class Battery:
    def battery_info(self):
        return "this is battery"



class Engine:
    def engine_info(self):
        return "this is engine"



class ElectricCar(Battery, Engine, Car):
    pass



my_new_car = ElectricCar("Tesla", "Model s")
print(my_new_car.battery_info())
print(my_new_car.engine_info())