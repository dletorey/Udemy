print('Today is a good day to learn Python')
print('Python is fun')
print("Python's strings are easy to use")
print('We can even include "quotes" in strings')
print('hello' + ' world')
greeting = "Hello"
name = "Dave"

# if we want we can add a space in here

print(greeting + " " + name)
age = 24
print(age)
print(type(greeting))
print(type(age))

age_in_words = "2 years"
print(age)
print(type(age))
# print(name + " is " + age + " years old")
print(name + f" is {age} years old") # putting an "f" before the string means you can use temperate literals like in JavaScript
print(f"Pi is approximately {22 /7:12.50f}")
pi = 22/7
print(f"Pi is approximately {pi:12.50f}")