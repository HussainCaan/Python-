class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def fullname(self):
        print(f"{self.brand} {self.model}")

mycar = Car("Honda", "Civic") 
# print("Model:", mycar.model) # Output: Model: Civic
# print("Model:", mycar.brand) # Output: Model: Civic 
# fullname=mycar.fullname() # Output: 'Honda Civic'
# print("Fullname:", fullname)

# Inheritence

class ElectricCar(Car):
    def __init__(self, battery_size, brand, model):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def battery_info(self):
        super().fullname()
        return f"{self.brand} {self.model} has a battery size of {self.battery_size} kWh"

my_electric_car = ElectricCar(75, "Tesla", "Model 3")
print("Battery Info:", my_electric_car.battery_info())