number = input("Enter a number: ")
sum = 0

for i in range(0, int(number)+ 1):
    if i % 2 == 0:
        sum += i
        
print(f"Sum of even number is: {sum}")