first_dict = {
    "name": "Alice",
    "age": 20,
    "city": "New York",
    "Series" : {
        "name": "Alice in Borderland",
        "seasons": 3,
        "genre": "Thriller"
    }
}

# print(first_dict["Series"]["name"]) # Output: "Alice in Borderland"
# print(first_dict.get("age")) # Output: 20
# # print(first_dict["namee"]) # This will raise a KeyError
# print(first_dict.get("namee")) # Output: None ---------- This is the difference between using [] and get() method
# first_dict["age"] = 21 # Updating age to 21
# first_dict["country"] = "USA" # Adding a new key-value pair
# del first_dict["city"] # Removing the key "city"
# print(first_dict)




# Loops through dictionary
for key in first_dict:
    if key != "Series":
        pass
        # print(f"{key}: {first_dict[key]}")
    else:
        print("Series Details:")
        for sub_key in first_dict["Series"]:
            # print(f" {sub_key}: {first_dict['Series'][sub_key]}")
            pass



for key, values in first_dict.items():
    if key!= "Series":
        # print(f"{key} : {values}")
        pass
    else:
        print("Series Details:")
        for subKey, subvalues in first_dict["Series"].items():
            # print(f" {subKey} : {subvalues}")
            pass

if "name" in first_dict:
    pass
    # print("Name key exists in the dictionary")

first_dict.pop("age") # Removes and returns the value associated with "age"  # This will raise a KeyError if "age" does not exist
# print(first_dict)
first_dict.popitem() # Removes and returns the last inserted key-value pair # This is useful in Python 3.7+ where dictionaries maintain insertion order
# print(first_dict)
 


# comphrehensions in dictionaries

Series_Values_keys = [values for values in first_dict["Series"].keys()] # Output: ['name', 'seasons', 'genre'] compiling keys of nested dictionary into a list
Series_Values_values = [values for values in first_dict["Series"].values()] # Output: ['Alice in Borderland', 3, 'Thriller'] compiling values of nested dictionary into a list

# print(Series_Values)
