# Coding Exercise 10 break
# Modify the code inside this loop to stop when i is exactly divisible by 11
for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break
print("-" * 15)

# Coding Exercise 11 continue
# Write a program to print out all the numbers from 0 to 20 that aren't divisible by 3 or 5.
# Zero is considered divisible by everything (zero should not appear in the output).
# The aim is to use the continue statement, but it's also possible to do this without continue.
for i in range(1, 20):
    if i % 3 == 0 or i % 5 == 0:
        continue
    else:
        print(i)

# Coding Exercise 12 augmented assignment in a loop
# Early computers could only perform addition. In order to multiply one number by another, they performed repeated addition.
# For example, 5 * 8 was performed by adding 5 eight times
# 5 + 5 + 5 + 5 + 5 + 5 + 5 + 5 = 40
# Use a for loop, and augmented assignment, to give answer the result of multiplying number by multiplier
# Paste your code into your IDE, and make sure it works with different values for number & multiplier
# Note that this exercise checking system will only validate your code with the values 5 and 8, for number and multiplier.

number = 5
multiplier = 8
answer = 0

# add your loop after this comment
for num in range(multiplier):
    answer += number
print(answer)
