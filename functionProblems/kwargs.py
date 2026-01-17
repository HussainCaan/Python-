# Kwargs are for keyword arguments, allowing you to pass a variable number of named arguments to a function.
# you can use **kwargs to send keyword value pairts to a function.


# def print_info(**kwargs):
#     print(kwargs)  # This will print the dictionary of keyword arguments received
#     print(**kwargs) # This will unpack the dictionary and print the individual key-value pairs
#     # We can iterate over kwargs since it's a dictionary
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
        
        
# print_info(name ="Alice", age=30, city="New York")
# print_info(product="Laptop", price=999.99, stock=50)
# print_info(language = "python") # you can pass any number of keyword 

# More complex example

database = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35, "city": "Chicago", "profession": "Engineer"},
]

def filter_data(**kwargs):
    # I want to get all entries that match a certain criteria
    data = kwargs['database']
    filtered = lambda data: [person for person in data if person.get('age',0) > 25]
    extracted_data = filtered(data)
    return extracted_data


result = filter_data(database=database)
print(result)  # Output: [{'name': 'Alice', 'age': 30, 'city': 'New York'}, {'name': 'Charlie', 'age': 35, 'city': 'Chicago', 'profession': 'Engineer'}]



# -------------------------------------------------------------------------------------------------------------------
# Another realistic example
def filter_data2(data, **filters):
    result = data
    
    if 'min_age' in filters:
        result = [p for p in result if p.get('age', 0) >= filters['min_age']]
    
    if 'city' in filters:
        result = [p for p in result if p.get('city') == filters['city']]
    
    return result

result2 = filter_data2(database, min_age=28, city="New York")
print(result2)  # Output: [{'name': 'Alice', 'age': 30, 'city': 'New York'}]