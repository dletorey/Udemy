# # exercise 60 iterating over a range
# for i in range(1, 20): # this will go from 1 to 19 as the last number in the range is not included
#     print("i is now {}".format(i))

# # coding exercise 8 For Loop
# # Write a program to print out all the numbers from 0 to 9.
# for i in range(0, 10):
#     print(i)

#Exercise 61 more about ranges

for i in range(10): # if you want to start at 0 then you can just add the end value
    print("i is now {}".format(i))
print("-" * 10)
for i in range(0, 10, 2): # if you want to step then you need to include a start value
    print("i is now {}".format(i))
print("-" * 10)
for i in range(10, -1, -1): # if you want to go backwards higher number first and then a negative step value
    print("i is now {}".format(i))
print("-" * 10)