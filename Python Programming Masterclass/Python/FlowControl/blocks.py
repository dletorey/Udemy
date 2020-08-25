#for i in range(1, 13):
#    print("Number {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
#    print("*" * 80)

# Exercise 42 if Statements
name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)
# Checking 18 or older
if age >= 18:
    print("You are old enough to vote")
    print("Please put an \"X\" in the box")
else:
    print("Please come back in {0} years".format(18 - age))
# reversed checking if younger than 18
if age < 18:
    print("Please come back in {0} years".format(18 - age))
else:
    print("You are old enough to vote")
    print("Please put an \"X\" in the box")