shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# steps through every item in the list and prints it
for item in shopping_list:
    print("Buy " + item)
print("-" *15)
# steps through every item in the list and prints it if it is not spam
for item in shopping_list:
    if item != "spam":
        print("Buy " + item)
print("-" *15)
# steps through every item in the list if the item is equal to eggs it continues, ie skips eggs
for item in shopping_list:
    if item == "eggs":
        continue
    print("Buy " + item)
print("-" *15)