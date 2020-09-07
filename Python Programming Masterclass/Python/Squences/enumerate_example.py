# for index, character in enumerate("abcdefghijkl"):
#     print(index, "\t", character)

# exercise 125 practical uses for unpacking tuples

for t in enumerate("abcdefghijklm"):
    index, character = t
    print(index, character)

index, character = (0, 'a')
print(index)
print(character)