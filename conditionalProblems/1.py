age = input("Enter your age: ")

if isinstance(age, str) and age.isdigit():
    age = int(age)
    if age < 0:
        print("Age cannot be negative.")
    elif age < 18:
        print("You are a minor.")
    elif age < 65:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")
else:
    print("Invalid input. Please enter a valid age.")