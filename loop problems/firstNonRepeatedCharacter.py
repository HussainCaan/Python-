given_string = "banana"

for char in given_string:
    if given_string.count(char) == 1:
        print(f"{char} is the first non repeated character")
        break        
