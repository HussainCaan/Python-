class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


mycar = Car("Honda", "Civic") 
print("Model:", mycar.model) # Output: Model: Civic
print("Model:", mycar.brand) # Output: Model: Civic 

