import random #imports the random module


def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)

highest = 10 # sets the highest possible number and makes it easy to change in one spot, here
answer = random.randint(1, highest) # generates a random nuber between 1 and highest using randint from the random module imported
print("the correct answer is {}".format(answer)) # TODO remove this later this is only for testing
print("Please guess a number between 1 & {}, to quit type 0: ".format(highest))
guess = int(input())

#Exercise 69 Challenge
while guess != answer:
    if guess == 0:
        break
    elif guess < answer:
        print("Guess Higher")
    elif guess > answer:
        print("Guess Lower")
    guess = int(input("Keep guessing or use 0 to quit "))
if guess == 0:
    print("You quit the game")
else:
    print("you guessed the correct answer")

# # Exercise 48 Challenge
# if guess == answer:
#     print("You guessed it first time")
# else:
#     if guess < answer:
#         print("Guess Higher")
#     else:
#         print("guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("2nd time lucky")
#     else:
#         print("Failure")

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





