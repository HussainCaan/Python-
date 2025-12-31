# Expressions
x = 1
y = 5
z = 10
# Python is very strong in handling numbers and provides various built-in operations for numerical data types.
# Normal operations like addition, subtraction, multiplication, and division can be performed using standard operators.
# Python intelligently handles large integers and floating-point numbers.
# Python numpy library is widely used for numerical computations, providing support for arrays, matrices, and a wide range of mathematical functions.

1 == 2 < 3 # This expression evaluates to False because 1 is not equal to 2. It will calculate it like (1 == 2) and (2 < 3)
1 < 2 < 3 # This expression evaluates to True because 1 is less than 2 and 2 is less than 3.

# Third party libraries like NumPy and Pandas enhance Python's capabilities for numerical computations, making it a popular choice for data analysis, scientific computing, and machine learning tasks.
# One of the popular libraries for numbers is Math library which provides various mathematical functions and constants.
import math
math.floor(4.7)  # Output: 4
math.ceil(4.2)   # Output: 5
math.floor(-4.7) # Output: -5
math.ceil(-4.2)  # Output: -4
math.trunc(4.7)  # Output: 4
math.trunc(-4.7) # Output: -4. trunc() removes the decimal part and goes towards zero.

int("123")    # Output: 123
float("123.45") # Output: 123.45
int(3.14)   # Output: 3
float(3)    # Output: 3.0


import random
random.random()        # Output: Random float between 0.0 to 1.0
random.randint(1, 10) # Output: Random integer between 1 and 10 (inclusive)
random.choice(['apple', 'banana', 'cherry']) # Output: Randomly selects one item from the list
random.shuffle([1, 2, 3, 4, 5]) # Shuffles the list in place
random.sample([1, 2, 3, 4, 5], 3) # Output: Randomly selects 3 unique items from the list
random.uniform(1.0, 10.0) # Output: Random float between 1.0 and 10.0
random.gauss(0, 1) # Output: Random float from a Gaussian distribution with mean 0 and standard deviation 1
random.seed(42) # Sets the seed for reproducibility of random numbers

# Python also supports complex numbers, which are numbers with a real and imaginary part.
complex_num = 2 + 3j
print(complex_num.real)      # Output: 2.0  
print(complex_num.imag)      # Output: 3.0
print(complex_num.conjugate()) # Output: (2-3j)
