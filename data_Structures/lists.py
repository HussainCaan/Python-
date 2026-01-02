Tea_Varieties = [
    "Black Tea",
    "Green Tea",
    "Oolong Tea",
    "White Tea",
    "Pu-erh Tea",
    "Herbal Tea",
    "Chai Tea",
]
Tea_Varieties[0] # Output: "Black Tea"
Tea_Varieties[3] # Output: "White Tea"
Tea_Varieties[-1] # Output: "Chai Tea" last item

Tea_Varieties[1:4] # Output: ['Green Tea', 'Oolong Tea', 'White Tea'] items from index 1 to 3
Tea_Varieties[:3] # Output: ['Black Tea', 'Green Tea', 'Oolong Tea'] first three items
Tea_Varieties[2:] # Output: ['Oolong Tea', 'White Tea', 'Pu-erh Tea', 'Herbal Tea', 'Chai Tea'] items from index 2 to end
# print(Tea_Varieties[-3:]) # Output: ['Herbal Tea', 'Chai Tea'] last three items

Tea_Varieties[3] = "Yellow Tea" # Changing "White Tea" to "Yellow Tea"

Tea_Varieties[1:2] = ["Matcha Tea", "Sencha Tea", "Kawa Tea"] # Replacing "Green Tea" with "Matcha" and "Sencha"

# for tea in Tea_Varieties:
#     print(tea, end="\n")  # Output: Black Tea-Matcha -Sencha-Oolong Tea-Yellow Tea-Pu-erh Tea-Herbal Tea-Chai Tea-
    
len(Tea_Varieties) # Output: 8 number of items in the list
Tea_Varieties.append("Earl Grey Tea") # Adding "Earl Grey Tea" to the end of the list
Tea_Varieties.insert(2, "Darjeeling Tea") # Inserting "Darjeeling Tea" at index 2
Tea_Varieties.remove("Kawa Tea") # Removing "Kawa Tea" from the list
popped_tea = Tea_Varieties.pop() # Removes and returns the last item "Earl Grey Tea"
# print(popped_tea)
# print(Tea_Varieties)

Tea_Varieties.sort() # Sorts the list in alphabetical order
Tea_Varieties.reverse() # Reverses the order of the list
Tea_Varieties.index("Oolong Tea") # Output: 4 finds the index of "Oolong Tea"
Tea_Varieties.count("Chai Tea") # Output: 1 counts how many times "Chai Tea" appears in the list
Tea_Varieties.extend(["Rooibos Tea", "Chamomile Tea"]) # Adding multiple items to the end of the list
Tea_Varieties_copy = Tea_Varieties.copy() 
Tea_varieties_deep_copy = list(Tea_Varieties) 
Tea_Varieties_new_Copy = Tea_Varieties[:] # Another way to create a shallow copy of the list


# List comprehensions provide a concise way to create lists.
squared_numbers = [x**2 for x in range(10)] # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
even_numbers = [x for x in range(20) if x % 2 == 0] # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
Uppercase_Tea_Varieties = [tea.upper() for tea in Tea_Varieties] # Converts each tea variety to uppercase
filtered_tea = [tea for tea in Tea_Varieties if "Sencha" in tea] # Filters the list to include only items containing "Tea"
# print(filtered_tea)


# Problems 
perfect_squares = [x**2 for x in range(1,10) if x**2 % x == 0]
# print(perfect_squares)

negative_values = [-1,-5, 3,-7]
absolute_values = [(x * -1) if x < 0 else x for x in negative_values]
# print(absolute_values)

lower_case = ['hello', 'world']
upper_case = [x.upper() for x in lower_case]
# print(upper_case)

given_list = ['cat', 'elephant', 'dog']
list_of_Length_of_words = [len(x) for x in given_list]
# print(list_of_Length_of_words)


# Intermediate problems to list comprehensions

nested_list = [[1, 2], [3, 4], [5, 6]]
flatend_list = [item for sublist in nested_list for item in sublist]
# print(flatend_list)

orignal_list = [1, 2, 3, 4]
number_square = [(x, x**2) for x in orignal_list]
# print(number_square)

complete_list = ['apple', 'banana', 'orange']
string_Start_Vowel = [x for x in complete_list if x[0] ==  'a' or x[0] == 'i' or x[0] =='u' or x[0] == 'o' or x[0] == 'e']
# print(string_Start_Vowel)


# get number greater than 5 and multiply by 2
random_list = [1, 6, 3, 8, 4]
solved_list = [x * 2 for x in random_list if x > 5]
# print(solved_list)

numbers = [1, 2, 3, 4]
result = [f'{numbers[i]}-{numbers[i+1]}' for i in range(0, len(numbers), 2)]
# print(result)

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combined_list = [f'{x}{y}' for x,y in zip(list1, list2)]
print(combined_list)