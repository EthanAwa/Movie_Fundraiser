def yes_no_checker(question):
    valid = False

    while not valid:

        error = "\nPlease answer with yes/no\n"
        response = input(question)

        if response == "yes" or response == "no":
            return response
        else:
            print(error)


loop = True
while loop:
    snack_check = yes_no_checker("Do you want to buy snacks? Type \"yes\" or \"no\" (No quotes): ")
    if snack_check == "yes":
        print("\nOk, what would you like to order: \n")
    else:
        print("\nOk, fair enough\n")
        loop = False
