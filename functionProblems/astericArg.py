def sum_all(*args):
    print(args)  # This will print the tuple of arguments received
    print(*args) # This will unpack the tuple and print the individual arguments
    # We can iterate over args since it's a tuple
    total = ""
    for num in args:
        total += num
    print("Total:", total)
    return sum(args) # for strings this will raise an error because sum() expects numbers

# print(sum(1, 2, 3, 4, 5))  # Output: 15
# print(sum(10, 20))        # Output: 30
print(sum_all(1,4,6,7,4))              # Output: 0 
# *args allows the function to accept any number of positional arguments. 

print(sum_all("hello", "world"))  # Output: helloworld