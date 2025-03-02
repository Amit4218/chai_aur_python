# Class variable

# Add a class variable to car that 
# keeps track of te number of cars created

class Car:

    total_car_created = 0
    
    def __init__(self, brand , model):
        self.__brand = brand
        self.model = model
        self.total_car_created += 1   # mostly used
        # Car.total_car_created += 1  // can be written like this too.

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
    
car_count = Car("Tata", "Safari")
print(car_count.total_car_created)

electric_car  = Electric_car("Tesla","Model s", "85KWh")
print(electric_car.total_car_created)