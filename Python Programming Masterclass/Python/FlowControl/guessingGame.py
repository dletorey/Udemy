answer = 5
print("Please guess a number between 1 & 10: ")
guess = int(input())

# Exercise 48 Challenge
if guess == answer:
    print("You guessed it first time")
else:
    if guess < answer:
        print("Guess Higher")
    else:
        print("guess lower")
    guess = int(input())
    if guess == answer:
        print("2nd time lucky")
    else:
        print("Failure")

# print("Please guess a number between 1 & 10: ")
# guess = int(input())
# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done you guessed it")
#     else:
#         print("Sorry you have not guessed correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done you guessed it")
#     else:
#         print("Sorry you have not guessed correctly")
# else:
#     print("You got it first time")





