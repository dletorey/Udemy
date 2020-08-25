day = "Saturday"
temperature = 30
raining = False

if (day == "Saturday" and temperature > 27) and not raining: # the brackets show precedence
    print("Go swimming")
else:
    print("Learn Python")