# Mutable are those data structures whose values can be changed after they have been created.
# Immutable are those data structures whose values cannot be changed after they have been created.
# Examples of IMMutable Data Structures
# username = "john_doe"  # String
# user_id = 12345       # Integer
# username = "jane_doe"  # Reassigning creates a new string object
# user_id = 67890       # Reassigning creates a new integer object

# print(username)
# print(user_id)

x = 10
y = x
print(x) # Output: 10
print(y) # Output: 10
x = 20 # Reassigning x to a new integer object
print(x) # Output: 20
print(y) # Output: 10 remiains unchanged Why is that? Because integers are immutable in Python. When we created x = 10 so x was assigned to integer object 10.
# And then when we did y = x, y was assigned to the same integer object 10. But when we reassigned x to 20, a new integer object 20 was created and x now points to that new object. y still points to the original integer object 10.
# That's the real meaning of immutability. The original object (10) remains unchanged, and any variable that was pointing to it (like y) still points to that unchanged object.


