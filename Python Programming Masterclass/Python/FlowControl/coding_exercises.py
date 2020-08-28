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