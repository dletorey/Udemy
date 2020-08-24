for i in range(1,13):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}" # the number after the colon is the width of the character
          .format(i, i ** 2, i ** 3)) # ** is to the power of

print()

for i in range(1,13):
    print("No. {0:<2} squared is {1:<4} and cubed is {2:^4}" # the less than < will left align the carat ^ will center
          .format(i, i ** 2, i ** 3)) # ** is to the power of

print()

print("Pi is appromximately {0:12}".format(22/7))
print("Pi is appromximately {0:12f}".format(22/7))
print("Pi is appromximately {0:12.50f}".format(22/7))
print("Pi is appromximately {0:52.50f}".format(22/7))
print("Pi is appromximately {0:62.50f}".format(22/7))
print("Pi is appromximately {0:72.50f}".format(22/7))