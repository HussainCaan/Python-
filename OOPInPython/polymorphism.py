class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand  # To make a variable private in python we have to use double Underscore before that in constructor
        self.__model = model
        self.total_car += 1
    def get_brand(self):
        return self.__brand
    def get_model(self):
        return self.__model
    def fullname(self):
        print(f"{self.__brand} {self.__model}")
    def fuel_type(self, typeofFuel):
        self.type = typeofFuel
        return self.type

        
class ElectricCar(Car):
    def __init__(self, battery_size, brand, model):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def battery_info(self):
        super().fullname()
        return f"{self.get_brand()} {self.get_model()} has a battery size of {self.battery_size} kWh"
    def fuel_type(self,typeofFuel):
        self.type = typeofFuel
        return self.type
    
my_electric_car = ElectricCar(75, "Tesla", "Model 3")
print(my_electric_car.fuel_type("Electricity"))  # Output: Electricity
my_car = Car("Honda", "Civic")
print(my_car.fuel_type("petrol"))  # Output: Petrol or Diesel
print("Total cars created:", Car.total_car)  # Output: Total cars created: 2 one by electric car and one by normal car