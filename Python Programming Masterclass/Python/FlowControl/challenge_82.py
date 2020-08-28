user_options = [
                "1 go shopping",
                "2 go for a bike ride",
                "3 go dancing",
                "4 go sky-diving"
                ]
print("Choose one of the following options:")
for i in user_options:
    print(i)
print("0 exit")
print()
while True:
    choice = int(input())
    if choice == 1:
        print("You choose", user_options[choice - 1])
        print("Choose another")
    elif choice == 2:
        print("You choose", user_options[choice - 1])
        print("Choose another")
    elif choice == 3:
        print("You choose", user_options[choice - 1])
        print("Choose another")
    elif choice == 4:
        print("You choose", user_options[choice - 1])
        print("Choose another")
    elif choice == 0:
        print("Goodbye")
        break
    else:
        print("You pressed {}. Please enter a valid option".format(choice))