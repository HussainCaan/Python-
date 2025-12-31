# Object type/data types

# In Python, everything is an object, and every object has a type.
# The type of an object determines what kind of data it holds and what operations can be performed on it.
# You can check the type of an object using the built-in type() function.
# Examples of different data types in Python:
# String
name = "Alice"
number = "12345"
print(type(name))   # Output: <class 'str'>
print(type(number)) # Output: <class 'str'>
# Integer
age = 30
print(type(age))    # Output: <class 'int'>
# Float 
height = 5.9
print(type(height)) # Output: <class 'float'>
# List
fruits = ["apple", "banana", "cherry"]
print(type(fruits)) # Output: <class 'list'>
# Tuple
coordinates = (10.0, 20.0)
print(type(coordinates)) # Output: <class 'tuple'>
# Dictionary
person = {"name": "Bob", "age": 25} # Key-Value pairs
print(type(person)) # Output: <class 'dict'>
# Set
unique_numbers = {1, 2, 3, 4, 5} # Set of unique numbers. In set duplicates are not allowed
print(type(unique_numbers)) # Output: <class 'set'>