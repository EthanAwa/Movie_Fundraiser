# Imports
import regex
import pandas


# Functions
def not_blank(question, error):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response

        else:
            print(error)


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


def get_snack():
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

    desired_snack = ""
    while desired_snack != "quit" or desired_snack != "q":

        snack_row = []

        desired_snack = input("Snack: ").lower()

        if desired_snack == "quit" or desired_snack == "q":
            return snack_order

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

        snack_row.append(amount)
        snack_row.append(snack_choice)

        if snack_choice != "quit" and snack_choice != "invalid choice":
            snack_order.append(snack_row)
        elif snack_choice == "quit":
            break

    return snack_order


def check_tickets(tickets_bought, ticket_limit):
    if tickets_bought == ticket_limit:
        print("All tickets have been sold, there are no more seats available")
        seats = False
    else:
        print(f"{tickets_bought} tickets have been sold, there are {ticket_limit - tickets_bought} seats available")
        seats = True
    return seats


def get_ticket_price():
    # Ask for age (12 - 130)

    age = int_check("How old are you? ")

    if age < 12:
        print("You are too young for this movie, sorry")
        return "invalid age"

    elif age > 130:
        print("Are you sure that you're {} years old? That looks like a mistake.".format(age))
        return "invalid age"
    # Calculate ticket prices

    if age < 16:
        ticket_cost = 7.50

    elif age >= 65:
        ticket_cost = 6.50

    else:
        ticket_cost = 10.50

    return ticket_cost


# Variables
name = ""
tickets_sold = 0
ticket_price = 0
profit = 0
max_tickets = 5  # Will be 150 for final version
loop = True
snack_order = []

# Main Routine

# Set up dictionaries / lists

# Ask user if they've used the program before

# Loop code for ticket details

while loop:
    seats = check_tickets(tickets_sold, max_tickets)

    while name != "quit":

        if seats:
            # Ask for name (can't be blank)
            name = not_blank("Please enter your name or type quit to stop booking seats: ",
                             "Please enter your name or quit, this can't be blank.\n")

            if name == "quit":
                loop = False
                break

            else:
                ticket_price = get_ticket_price()
                if ticket_price == "invalid age":
                    continue

                print("That'll be ${:.2f} total\n".format(ticket_price))
                print("Here's your ticket, enjoy the movie\n")
                tickets_sold += 1
                profit += ticket_price - 5

            seats = check_tickets(tickets_sold, max_tickets)
        else:
            print("Profit: ${:.2sf}".format(profit))
            loop = False
            break
        # Added to see when the loop has ended, will change places as code develops
    # Loop to ask for snacks

    # Calculate snack prices

    # Ask for payment (apply 5% surcharge if credit card)

# Calculate total ticket and snack cost

# Save to a text / csv file
