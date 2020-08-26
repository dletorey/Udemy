# # Exercise 57 for Loops
# parrot = "Norwegian Blue"
#
# for character in parrot:
#     print(character)

# #Exercise 58 Stepping through a for Loop
# # number = "9,423;456:292,747;327:272 849,939;535"
# number = input("Please enter a series of numbers with whichevr seperator you like: ")
# seperators = ""
#
# for char in number:
#     if not char.isnumeric():
#         seperators = seperators + char
#
# print(seperators)
#
# values = "".join(char if char not in seperators else " " for char in number).split()
# print([int(val) for val in values])
# print(sum([int(val) for val in values]))

#Coding Exercise 7 Extracting Capitals
# Write a program to print out the capital letters in the string quote

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.
caps = ""
for char in quote:
    if char.isupper():
        caps = caps + char
print(caps)