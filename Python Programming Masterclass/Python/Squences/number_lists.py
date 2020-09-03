even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
# print(min(even))
# print(max(even))
# print(min(odd))
# print(max(odd))
# print("-" * 6)
# print(len(even))
# print(len(odd))
#
# print("-" * 6)
# print("mississippi".count("s"))

# exercise 99 sorting lists
even.extend(odd)
print(even)
even.sort()
print(even)
even.sort(reverse=True)
print(even)