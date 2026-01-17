class Car:
    def __init__(self, brand, model):
        self.__brand = brand  # To make a variable private in python we have to use double Underscore before that in constructor
        self.__model = model
    def get_brand(self):
        return self.__brand
    def get_model(self):
        return self.__model
    def fullname(self):
        print(f"{self.__brand} {self.__model}")
        
class ElectricCar(Car):
    def __init__(self, battery_size, brand, model):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def battery_info(self):
        super().fullname()
        return f"{self.get_brand()} {self.model} has a battery size of {self.battery_size} kWh"
    
my_electric_car = ElectricCar(75, "Tesla", "Model 3")
print("Battery Info:", my_electric_car.battery_info())