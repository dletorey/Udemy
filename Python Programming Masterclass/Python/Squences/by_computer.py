available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mouse mat",
                   "hdmi cable",
                   "dvd drive",
                   "track pad",
                   "printer"]
# valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)
current_choice = "-"
computer_parts = [] # create an empty list to store the items

while current_choice != '0':
    if current_choice in valid_choices:
        index = int(current_choice) -1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            # it's already in the list, so remove it
            computer_parts.remove(chosen_part)
        else:
            computer_parts.append(chosen_part)
        print("Your list now includes {}.".format(computer_parts))
        # print("Adding {}, to computer shopping list".format(current_choice))
        # if current_choice == "1":
        #     computer_parts.append("computer")
        # elif current_choice == "2":
        #     computer_parts.append("monitor")
        # elif current_choice == "3":
        #     computer_parts.append("keyboard")
        # elif current_choice == "4":
        #     computer_parts.append("mouse")
        # elif current_choice == "5":
        #     computer_parts.append("mousemat")
        # elif current_choice == "6":
        #     computer_parts.append("hdmi cable")
    else:
        print("Please add options from the list below:")
        for number, part in enumerate(available_parts):
            print("{0}:\t{1}".format(number + 1, part))
        print("0:\tto finish")
    current_choice = input()
print(computer_parts)