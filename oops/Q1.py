# Basic Class and Object
# Create a car class with attribute like brand and models.
# Then create an instance of this class

# __init__ is also known as constructer


class Car:
    
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model



my_car = Car("Toyota", "corolla")
print(my_car.brand)
print(my_car.model)

car_2 = Car("Tata", "safari")
print(car_2.brand)
print(car_2.model)
