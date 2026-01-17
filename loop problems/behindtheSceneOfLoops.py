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
# print(f.readlines()) # this will read all the lines
print(f.read()) # this will read the whole file