# Class Method and self
# Add a method ta the class that displays the full
# name of the car (brand and model)


class Car:
    
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"


car = Car("Toyota", "Supra")
print(car.full_name())
print(car.brand)
print(car.model)



