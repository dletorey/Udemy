name = input("What is your name? ")
age = int(input("How old are you {}? ".format(name)))
if 18 <= age < 31:
    print("Great {}, you can attend the 18-30 holidy".format(name))
else:
    if age < 18:
        print("{}, you're not yet old enough to come on an 18-30 holiday, come back in {} years.".format(name, 18 - age))
    else:
        print("{} try a more sedate holiday you'd hate the kids anyway".format(name))