#         01234567890123
#         43210987654321
parrot = "Norwegian Blue"
print(parrot)

print(parrot[0:6]) # Norweg
print(parrot[-14:-8]) # Norweg
print(parrot[3:5]) # we
print(parrot[-11:-9]) # we
print(parrot[0:9]) # Norwegian
print(parrot[-14:-5]) # Norwegian
print(parrot[:9]) # Norwegian starting at the begining you don't need a start value
print(parrot[:-5]) # Norwegian starting at the begining you don't need a start value
print(parrot[10:14]) # Blue
print(parrot[-4:]) # Blue
print(parrot[-4:]) # Blue if you leave off the end value it prints to the end
print(parrot[:])
print(parrot[:9] + parrot[10:])
print(parrot[:-5] + parrot[-4:])

print()
print(parrot[-4:-2])
print(parrot[-4:12])