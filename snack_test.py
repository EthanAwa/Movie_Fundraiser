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

# mock up of snacks
snacks = {"popcorn": 2.50, "m&m": 3.00, "pc": 4.50, "oj": 3.25, "water": 2.00}
snack_list = ["popcorn", "m&ms", "pita chips", "orange juice", "water"]

loop = True
while loop:
    print("We have popcorn, m&ms, pita chips, orange juice, and water for sale. Please enter what one you would like "
          "based on the options list")
    choice = string_checker("snack (options are popcorn, m&m, pc, oj, and water): ", snacks.keys())
    amount = int_check("How many would you like (maximum of 4): ")

    if amount > 4:
        print("You can only buy up to 4 snacks at a time, sorry ")
    else:
        price = snacks[choice] * amount

    print("You ordered: {} x {}")