def yes_no_checker(question):
    valid = False

    while not valid:

        error = "\nPlease answer with yes/no or y/n\n"
        response = input(question).lower()

        if response == "yes" or response == "no":
            return response
        elif response == "y" or response == "nn":
            return response
        elif response == "quit":
            return response
        else:
            print(error)


loop = True
while loop:
    snack_check = yes_no_checker("Do you want to buy snacks? Type \"yes\" or \"no\" (No quotes, y/n also work): ")
    if snack_check == "yes" or snack_check == "y":
        print("\nOk, what would you like to order: \n")
    elif snack_check == "no" or snack_check == "n":
        print("\nOk, fair enough\n")
    else:
        loop = False
        break
