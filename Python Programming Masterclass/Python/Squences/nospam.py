menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "tomato", "spam"], # the last comma will be ignored but adding more items means to the list is eaiser and the git update would only mention the extra lines in the commit not the line with added comma
]
# # my solution to no spam
# for meal in menu:
#     for item in meal:
#         if "spam" != item:
#             print(item, end=' ')
#     print()
# solution 1
for meal in menu:
    for index in range(len(meal) -1, -1, -1):
        if meal[index] == "spam":
            del meal[index]
    print(", ".join(meal))
