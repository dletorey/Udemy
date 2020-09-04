pangram = "The quick brown fox jumps over the lazy dog"

words = pangram.split() # split returns a list using whitespace characters
print(words)

numbers = "9,234,5343,2214,32,324,23423,54"
print(numbers.split(","))
seperators = ","
generated_list = "".join(char if char not in seperators else " " for char in numbers).split()
print(generated_list)
print([int(val) for val in generated_list])