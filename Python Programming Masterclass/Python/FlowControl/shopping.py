shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# # Exercise 63 continue
# # steps through every item in the list and prints it
# for item in shopping_list:
#     print("Buy " + item)
# print("-" *15)
# # steps through every item in the list and prints it if it is not spam
# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)
# print("-" *15)
# # steps through every item in the list if the item is equal to eggs it continues, ie skips eggs
# for item in shopping_list:
#     if item == "eggs":
#         continue
#     print("Buy " + item)
# print("-" *15)

# # Exercise 64 break
#
# for item in shopping_list:
#     if item == "eggs":
#         break # when the item is equal to eggs the loop will stop
#     print("Buy " + item)
# print("-" * 15)
#
# item_to_find = "spam"
# found_at = None
#
# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break # this break will stop the loop once instance of item_to_find is reached, this could be left out if you wanted to find multiple indexes
# print("Item found at position {}".format(found_at))
# print("-" * 15)

# Exercise 65 Initialising variables & None

item_to_find = "bananas"
found_at = None

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break # this break will stop the loop once instance of item_to_find is reached, this could be left out if you wanted to find multiple indexes
if found_at is not None: # this condition checks to see if found_at has been updated
    print("Item found at position {}".format(found_at))
else: # otherwise prints the next statment
    print("{} not found in list".format(item_to_find))
# this example is not the best a more succinct way is below
print("-" * 15)
if item_to_find in shopping_list: #checks if item is in list
    found_at = shopping_list.index(item_to_find) # sets found_at to be the index position of item
if found_at is not None: # this condition checks to see if found_at has been updated
    print("Item found at position {}".format(found_at))
else: # otherwise prints the next statment
    print("{} not found in list".format(item_to_find))
print("-" * 15)