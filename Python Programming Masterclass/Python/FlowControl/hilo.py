low = 1
high = 1000
guesses = 1
print("Please think of a number between {} and {}".format(low, high))
input("Please press enter to start")
guess = 1
allowed_chars = ["h", "l", "c"]
while low != high:
    guess = low + (high - low) // 2
    high_low = input("My guess is {0}. "
                     "Should I guess higher or lower or is {0} correct? "
                     "Enter h, l or c"
                     .format(guess)).casefold()
    if high_low == "h":
        # Guess higher. The low end becomes 1 greater than the guess
        low = guess + 1
        print()
    elif high_low == "l":
        # Guess Lower. The high end becomes 1 less than the guess
        high = guess - 1
        print()
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h, l or c")
    if high_low in allowed_chars:
        guesses += 1 # guesses = guesses + 1 updated this to make it an augmented assignment
else:
    print("You thought of the number {0}. I got it in {1} guesses.".format(low, guesses))