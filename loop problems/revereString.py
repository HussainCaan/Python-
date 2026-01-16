input_string = "Python"
Reversed_String = ""

# As string are immutable in Python, so we can do this (Important concept)
for char in input_string:
    Reversed_String = char + Reversed_String
    
print(Reversed_String)