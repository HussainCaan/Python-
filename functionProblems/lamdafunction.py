# A function without a name is called a lambda function.
# Lambda functions are used for small, throwaway functions that are not going to be reused elsewhere in the code.
# They are defined using the lambda keyword followed by the parameters, a colon, and the expression to be evaluated.
# The syntax of a lambda function is:

result = lambda parameter: parameter ** 3 # No name for the right side of the equal sign but it's assigned to the variable 'result' and will store that lambda function value. 
# Complex problems using lambda
database = [
    {'name': 'Alice', 'age': 30, 'city': 'New York'},
    {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'},
    {'name': 'Charlie', 'age': 35, 'city': 'Chicago'},  
    {'name': 'David', 'age': 28, 'city': 'Miami'},
    {'name': 'Eve', 'age': 22, 'city': 'Seattle'}
]

database_extraction =  lambda data: [person for person in data if person['age'] > 28 and person['city'] in ['New York', 'Chicago']]
extracted_data = database_extraction(database) # database_extraction is a lambda function that takes 'data' as input and returns a list of people from the database who are older than 28 and live in either New York or Chicago.
print(extracted_data) # Output: [{'name': 'Alice', 'age': 30, 'city': 'New York'}, {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}]
print(database_extraction) # OUTPUT: <function <lambda> at 0x000001558686F100> # This will print the memory address of the lambda function stored in the variable database_extraction