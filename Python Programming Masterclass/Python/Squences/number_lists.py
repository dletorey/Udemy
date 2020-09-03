# # even = [2, 4, 6, 8]
# # odd = [1, 3, 5, 7, 9]
# # # print(min(even))
# # # print(max(even))
# # # print(min(odd))
# # # print(max(odd))
# # # print("-" * 6)
# # # print(len(even))
# # # print(len(odd))
# # #
# # # print("-" * 6)
# # # print("mississippi".count("s"))
# #
# # # exercise 99 sorting lists
# # even.extend(odd)
# # print(even)
# # even.sort()
# # print(even)
# # even.sort(reverse=True)
# # print(even)
#
# # exercise 103 creating lists
# empty_list = []
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
# numbers = even + odd
# print(numbers)
# sorted_numbers = sorted(numbers)
# print(sorted_numbers)
# print(numbers)
#
# digits = list("432985617")
# print(digits)
#
# # more_numbers = list(numbers) # this copies a list using the list class
# # more_numbers = numbers[:] # this copies the list using the slice method
# more_numbers = numbers.copy() # this copies the list using the copy function
# print(more_numbers)
# print(numbers is more_numbers)
# print(numbers == more_numbers)

# exercise 114 Nested Lists
empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
numbers = [even, odd]
print(numbers)

for number_list in numbers:
    print(number_list)
    
    for value in number_list:
        print(value)