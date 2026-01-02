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

Tea_Varieties[1:2] = ["Matcha", "Sencha", "Kawa"] # Replacing "Green Tea" with "Matcha" and "Sencha"
print(Tea_Varieties)