# # Exercise 57 for Loops
# parrot = "Norwegian Blue"
#
# for character in parrot:
#     print(character)

#Exercise 58 Stepping through a for Loop
# number = "9,423;456:292,747;327:272 849,939;535"
number = input("Please enter a series of numbers with whichevr seperator you like: ")
seperators = ""

for char in number:
    if not char.isnumeric():
        seperators = seperators + char

print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])
print(sum([int(val) for val in values]))