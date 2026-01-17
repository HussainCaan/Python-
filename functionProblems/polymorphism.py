# An operator double function that can handle both integers and strings.

def polymorphic_function(a, b):
    return a * b

# Testing the polymorphic_function with integers
result_int = polymorphic_function(5, 10)
print(f"Result with integers: {result_int}")  # Output: 15
# Testing the polymorphic_function with strings
# In the above code, the function polymorphic_function takes two parameters a and b.
# It uses the + operator which behaves differently based on the data types of a and b.
result_str_int = polymorphic_function('a' ,5) 
print(f"Result with string and integer: {result_str_int}")  # Output: 'aaaaa'
print(polymorphic_function('a' ,5))  # Output: aaaaa # This will print 'a' 5 times because the * operator when used with a string and an integer repeats the string that many times.
print(polymorphic_function(3 , 'b'))  # Output: bbb # This will print 'b' 3 times because the * operator when used with a string and an integer repeats the string that many times.