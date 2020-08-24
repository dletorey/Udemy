string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"
print(string1 + string2 + string3 + string4 + string5)
print("Hello " * 5)
print("Hello " * (5 + 4)) # Prints 9 times
print("Hello " * 5 + "4") # Prints 5 times with the number 4 at the end

today = "Monday"
print("day" in today)       # returns True because day is in the word Monday
print("Mon" in today)       # returns True because Mon is in the word Monday
print("Fri" in today)       # returns False because Fri is not in the word Monday
