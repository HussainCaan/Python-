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

# print(first_dict["Series"]["name"])

Series_Values = [values for values in first_dict["Series"].keys()]
print(Series_Values)