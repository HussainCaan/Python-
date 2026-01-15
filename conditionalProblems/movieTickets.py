age = input("Enter your age: ")
day = input("Enter the day of the week: ").strip().lower()
ticker_price = 0
if isinstance(age, str) and age.isdigit():
    if day != "wednesday":
        if int(age) >= 18:
            print("your ticket price is $18")
        else:
            print("Ticket price is $8")
    else:
        if int(age) >= 18:
            discount = 12 * .02
            ticker_price = 12 - discount
            print(f"Ticket price is {ticker_price}")
        else:
            discount = 8 * .02
            ticker_price = 8 - discount
            print(f"Ticket price is {ticker_price}")
else:
    print("wrong input")