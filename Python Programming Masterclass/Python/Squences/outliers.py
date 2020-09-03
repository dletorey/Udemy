# data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191, 350, 360]
# # del data[0:2]
# # print(data)
# # del data[14:]
# # print(data)
#
# min_valid = 100
# max_valid = 200
#
# for index, value in enumerate(data):
#     if (value < min_valid) or (value > max_valid):
#         del data[index]
# print(data)

# exercise 106 safely removing items from a list
data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]
min_valid = 100
max_valid = 200

# process low values in list

stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break
print(stop) # for debugging
del data[:stop]
print(data)

# process high values in the list
start = 0
for index in range(len(data) -1, -1, -1):
    # print(index)
    if data[index] <= max_valid:
        start = index + 1 # this is because the index will be the first value in the range
        break
print(start) # for debugging
del data[start:]
print(data)