age =50
print("My age is " + str(age) + " years") # str(age) coerces an integer into a str
print("My age is {0} years".format(age))
print("there are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "jan", "Mar", "May", "July", "Aug", "Oct", "Dec"))
print("J: {2}, F: {0}, M: {2}, A: {1}, M: {2}, J: {1}, J: {2}, A: {2}, S: {1}, O: {2}, N: {1}, D: {2}"
      .format(28, 30, 31))