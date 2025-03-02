# Class Ingeritance and isinstances() Function

# Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and Electric_car

# isinstance => returns a boolean value  # can be used to check which class does an instance  belong.

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
    

my_tesla = Electric_car('Tesla', "Model s", "85KWh")

print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, Electric_car))

    
