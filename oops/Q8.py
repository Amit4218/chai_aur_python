# Property Decorators

# Use a property decorater in the Car class to make the model attribute read only



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
    
car = Car("Tesla","model s")
# car.model = "city" // now we cant change the value
print(car.model) # this is the model method not the parameter
