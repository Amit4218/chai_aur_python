# Encapulation => to make something private

# Modify the Car to encapsulate the brand attribute
# making it private and provide a getter method for it

# use double undeScore "__" and the variable name, 
# to make a variable private Eg: __name 



class Car:
    
    def __init__(self, brand , model):
        self.__brand = brand
        self.model = model

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def get_brand(self):
        return self.__brand


class Electric_car(Car):

    def __init__(self, brand , model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


car = Car("Tata", "safari")
# print(car.__brand) => wont work now
print(car.get_brand())

