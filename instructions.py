def string_check(choice, options):
    for var_list in options:
        if choice in var_list:
            chosen = var_list[0].title()
            is_valid = "yes"
            break
        else:
            is_valid = "no"
    if is_valid == "yes":
        return chosen
    else:
        print("Sorry, that isn't a valid response")
        return "invalid choice"


def instructions(choice):
    show_help = "invalid choice"
    while show_help == "invalid choice":
        show_help = input("Would you like to read the instructions? (yes/no) ").lower()
        show_help = string_check(show_help, yes_no)

    if show_help == "Yes":
        print("Instructions on how to use the program")
        print("1. Enter your name, and how old you are. (Note, age ranges from 12 minimum to 130 maximum inclusive)")
        print("2. The program will then ask you if you would like snacks or not.")
        print("3. If you would like snacks, you enter them by typing a number, then the snack name (e.g 4popcorn = 4 x "
              "popcorn, 2juice = 2 x orange juice).\n   However, you can only have 4 of a snack maximum per ticket, "
              "even if you type 4 of a snack twice. It's apart of company policy, sorry.\n   Once you are done "
              "ordering, "
              "type quit or q to stop ordering")
        print("4. Then, choose whether to pay with cash or credit. There is a 5% surcharge fee when paying with "
              "credit, as to not annoy the banks.")
        print("5. To end the program at any time, type quit or q when you get asked your name.")


yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

instructions(yes_no)
print()
print("Program launches...")