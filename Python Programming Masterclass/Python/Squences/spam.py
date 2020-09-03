menu = [
        ["egg", "bacon"],
        ["egg", "sausage", "bacon"],
        ["egg", "spam"],
        ["egg", "bacon", "spam"],
        ["egg", "bacon", "sausage", "spam"],
        ["spam", "bacon", "sausage", "spam"],
        ["spam", "egg", "spam", "spam", "bacon", "tomato", "spam"], # the last comma will be ignored but adding more items means to the list is eaiser and the git update would only mention the extra lines in the commit not the line with added comma
]
for meal in menu:
        if "spam" not in meal:
                print(meal)
                for  item in meal:
                        print(item)
        else:
                print("{0} has a spam score of {1}"
                      .format(meal, meal.count("spam")))