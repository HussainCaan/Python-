class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def fullname(self):
        return f"{self.brand} {self.model}"

mycar = Car("Honda", "Civic") 
print("Model:", mycar.model) # Output: Model: Civic
print("Model:", mycar.brand) # Output: Model: Civic 
fullname=mycar.fullname() # Output: 'Honda Civic'
print("Fullname:", fullname)