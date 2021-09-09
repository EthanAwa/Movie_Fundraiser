import regex


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


# Set case for regex to match with
number_regex = "^[1-9]"

# List of all valid snacks and possible abbreviations
valid_snacks = [
    ["popcorn", "p", "corn"],
    ["M&M's", "mms", "m&ms", "m"],
    ["pita chips", "chips", "pc", "c"],
    ["water", "w"],
    ["orange juice", "oj", "juice"],
]

yes_no = [
    ["yes", "y"],
    ["no", "n"],
    ["quit", "q"]
]

snack_order = []

check_snack = "invalid choice"
while check_snack == "invalid choice":
    want_snack = input("Do you want to order snacks? ").lower()
    check_snack = string_check(want_snack, yes_no)

if check_snack == "Yes":

    desired_snack = ""
    while desired_snack != "quit" or desired_snack != "q":
        desired_snack = input("Snack: ").lower()

        if desired_snack == "quit" or desired_snack == "q":
            break

        if regex.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]

        else:
            amount = 1
            desired_snack = desired_snack

        desired_snack = desired_snack.strip()

        snack_choice = string_check(desired_snack, valid_snacks)

        if amount >= 5:
            print("Sorry, we have a 4 snack maximum")
            snack_choice = "invalid choice"

        if snack_choice != "quit" and snack_choice != "invalid choice":
            order = f"{amount} x {snack_choice}"
            snack_order.append(order)
        elif snack_choice == "quit":
            break

# Show order
print()
if len(snack_order) == 0:
    print("Snacks Ordered: None")
    print("Enjoy the movie")
else:
    print("Snacks Ordered:")

    for item in snack_order:
        print(item)

    print("Enjoy the snacks and the movie")
