current_choice = "-"
computer_parts = [] # create an empty list to store the items

while current_choice != '0':
    if current_choice in "12345":
        print("Adding {}, to computer shopping list".format(current_choice))
        if current_choice == "1":
            computer_parts.append("computer")
        elif current_choice == "2":
            computer_parts.append("monitor")
        elif current_choice == "3":
            computer_parts.append("keyboard")
        elif current_choice == "4":
            computer_parts.append("mouse")
        elif current_choice == "5":
            computer_parts.append("mousemat")
    else:
        print("Please add options from the list below:")
        print("1:\tcomputer")
        print("2:\tmonitor")
        print("3:\tkeyboard")
        print("4:\tmouse")
        print("5:\tmouse mat")
        print("0:\tto finish")
    current_choice = input()
print(computer_parts)