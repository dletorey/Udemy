low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Please press enter to start")
guess = 1
while True:
    guess = low + (high - low) // 2
    high_low = input("My guess is {0}. "
                     "Should I guess higher or lower or is {0} correct? "
                     "Enter h, l or c"
                     .format(guess)).casefold()
    if high_low == "h":
        # Guess higher
        print()
    elif high_low == "l":
        # Guess Lower
        print()
    elif high_low == "c":
        print("I got it in {} guesses!".format(guess))
        break
    else:
        print("Please enter h, l or c")