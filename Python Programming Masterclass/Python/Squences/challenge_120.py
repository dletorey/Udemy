generated_list = ['9', '234', '5343', '2214', '32', '324', '23423', '54']
print(generated_list)
print([int(val) for val in generated_list])

print(generated_list)
print("-" * 10)
integer_values = []
for value in generated_list:
    integer_values.append(int(value))
print(integer_values)

print("-" * 10)

for index in range(len(generated_list)):
    generated_list[index] = int(generated_list[index])

print(generated_list)

