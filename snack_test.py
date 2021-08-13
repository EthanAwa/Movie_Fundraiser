def string_checker(question, options):
    valid = False

    while not valid:

        response = input(question).lower()

        if response in options:
            return response
        elif response == "quit":
            return response
        else:
            for item in options:
                if response == item[0]:
                    return item

        print("Sorry, that isn't a valid response.")


def int_check(question):
    error = "Please enter a whole number that is more than 0 (1, 2, 3...)\n"

    valid = False
    while not valid:

        try:
            response = int(input(question))

            if response <= 0:
                print(error)

            else:
                return response

        except ValueError:
            print("Please enter a whole number only, not a decimal (e.g 3.0) "
                  "or a word (e.g Three)")


price = 0.00
loop = True

# mock up of snacks
snacks = ["popcorn", "m&m", "pc", "oj", "water"]
prices = [2.50, 3, 4.50, 3.25, 2]
snack_list = ["popcorn", "m&ms", "pita chips", "orange juice", "water"]

# Starting message, loops if in the while loop
print("We have popcorn, m&ms, pita chips, orange juice, and water for sale. \nPlease enter what one you would "
      "like based on the options list. \nYou can also choose not to stop ordering snacks by typing quit at the "
      "snack selection area, or no at the very start.\n")


while loop:

    choice = string_checker("What snack would you like? (options are popcorn, m&m, pc, oj, and water): ", snacks)

    if choice == "quit":
        print("Thank you for purchasing snacks, enjoy the movie")
        loop = False
        break

    else:
        amount = int_check("How many would you like (maximum of 4): ")

        if amount > 4:
            print("You can only buy up to 4 snacks at a time, sorry \n")

        if choice in snacks:
            item = snacks.index(choice)
            price = prices[item] * amount

            print("\nYou ordered: {} x {}. That costs ${:.2f}\n".format(amount, snack_list[item], price))
