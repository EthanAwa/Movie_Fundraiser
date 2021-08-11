def string_checker(question, options):
    valid = False

    while not valid:

        response = input(question).lower()

        if response in options:
            return response
        else:
            for item in options:
                if response == item[0]:
                    return item

        print("Sorry, that isn't a valid response.")

loop = True
while loop:
    snack_check = yes_no_checker("Do you want to buy snacks? Type \"yes\" or \"no\""
                                 "(No quotes, y/n also work): ", ["yes", "no", "quit"])
    if snack_check == "yes" or snack_check == "y":
        print("Ok, what would you like to order: ")
    elif snack_check == "no" or snack_check == "n":
        print("Ok, fair enough")
    elif snack_check == "quit":
        loop = False
        break
