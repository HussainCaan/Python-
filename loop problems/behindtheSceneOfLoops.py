# In python loops are used to repeat a block of code multiple times.
# Behind the scenes, loops work by using an iterator to keep track of the current position in a sequence.
# When an iteration tool (like a for loop) is used for an iterable (like a list or a string), Python creates an iterator object called __next__.
# The __next__ method retrieves the next item from the iterator each time it is called, until there are no more items left, at which point it raises a StopIteration exception.
# File is a little bit advanced but it gives you an idea of how loops work behind the scenes.

import time

print("Counting to 5 with a delay:")
username = "Hussain"
print(f"Hello, {username}!")

f = open("revereString.py")
# print(f.readline()) # this will read the first line
# print(f.readlines()) # this will read all the lines  This method is now less commonly used because it loads all lines into memory at once.
# print(f.read()) # this will read the whole file

# for line in f:
#     print(line, end='')  # end='' to avoid double newlines
#     time.sleep(1)  # Adding a delay of 1 second between printing each line
# f.close()
# In the above code, we opened a file named 'revereString.py' and used a for loop to read and print each line one by one with a delay of 1 second.
# This demonstrates how the for loop uses an iterator to go through each line in the file until

list1 = [1, 2, 3, 4, 5]
I = iter(list1)  # Creating an iterator object from the list named as I
print(I) # This will print the iterator object OUTPUT: <list_iterator object at 0x000001C5167D5150> this means that I is an iterator object and points to the memory address 0x000001C5167D5150
# Now if we do this

I.__next__()  # This will return the first element of the list OUTPUT: 1 but the I pointer will not move to the next element it's the __next__ method that moves the pointer to the next element and for the second I.__next__() call it will return 2 and so on.
print(I.__next__())  # OUTPUT: 1
print(I.__next__())  # OUTPUT: 2
print(I.__next__())  # OUTPUT: 3
print(I.__next__())  # OUTPUT: 4
print(I.__next__())  # OUTPUT: 5
# If we call I.__next__() again it will raise StopIteration exception because there are no more elements left in the list
# This is how loops work behind the scenes in Python using iterators and the __next__ method.


# NOte: This iter object is by defauly in files 
# For example
f = open("revereString.py")
# Now we don't have to do 'iter(f)' because f is already an iterator object by default in python
print(f.__next__())  # This will print the first line of the file
print(f.__next__())  # This will print the second line of the file
print(f.__next__())  # This will print the third line of the file
# and so on until the end of the file is reached. the end of the file is reached.
f.close()
# This is how file objects work as iterators in Python.
