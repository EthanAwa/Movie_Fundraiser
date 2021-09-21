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
        ["Popcorn", "p", "corn"],
        ["M&Ms", "mms", "m&ms", "m"],
        ["Pita Chips", "chips", "pc", "c"],
        ["Water", "w"],
        ["Orange Juice", "oj", "juice"],
    ]
    snack_order = []
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
ticket_sales = 0
profit = 0.0
max_tickets = 5  # Will be 150 for final version
loop = True
snack_order = []
count = 0
all_orders = []

# For data-frame
all_names = []
all_tickets = []
popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []
surcharge = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

# Data Frame Dictionary
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets,
    'Popcorn': popcorn,
    'Water': water,
    "Pita Chips": pita_chips,
    'M&Ms': mms,
    'Orange Juice': orange_juice,
    'Surcharge Multi': surcharge
}

price_dict = {
    "Popcorn": 2.5,
    "Water": 2,
    "Pita Chips": 4.5,
    "M&Ms": 3,
    "Orange Juice": 3.25
}

# List for valid yes/no responses
yes_no = [
    ["yes", "y"],
    ["no", "n"],
    ["quit", "q"]
]

# Payment methods
pay_method = [
    ["credit", "cr"],
    ["cash", "ca"]
]

# Main Routine

# Ask user if they've used the program before

# Loop code for ticket details

while name != "quit" and tickets_sold < max_tickets:
    seats = check_tickets(tickets_sold, max_tickets)

    name = not_blank("Please enter your name or type quit to stop booking seats: ",
                     "Please enter your name or quit, this can't be blank.\n")
    order = []

    # End loop if exit code is entered
    if name == "quit" or name == "q":
        break

    # Work out ticket price based on ago
    ticket_price = get_ticket_price()

    if ticket_price == "invalid age":
        continue

    tickets_sold += 1
    ticket_sales += ticket_price

    # Add name and ticket price to lists
    all_names.append(name)
    all_tickets.append(ticket_price)

    # Loop to ask for snacks
    check_snack = "invalid choice"
    while check_snack == "invalid choice":
        want_snack = input("Do you want to order snacks? ").lower()
        check_snack = string_check(want_snack, yes_no)

    if check_snack == "Yes":
        print("The snacks we have for sale are Popcorn, Pita Chips, Water, Orange Juice, and M&Ms. We also have a 4 "
              "snack at a time maximum policy")
        order = get_snack()
    else:
        order = []

    # Show order
    if len(order) == 0:
        print("Snacks Ordered: None")
        print("Enjoy the movie")
    else:
        print("Snacks Ordered:")
        print(order)

    all_orders.append(order)

    # Calculate snack prices

    # Ask for payment (apply 5% surcharge_mult if credit card)
    how_pay = "invalid choice"
    while how_pay == "invalid choice":
        how_pay = input("Please choose a payment method (cash or credit): ").lower()
        how_pay = string_check(how_pay, pay_method)

    if how_pay == "credit":
        surcharge_multi = 0.05
    else:
        surcharge_multi = 0

    surcharge.append(surcharge_multi)

    print()

# Check for number of snacks
for client_order in all_orders:
    # Assume no snacks have been ordered
    for item in snack_lists:
        item.append(0)

    snack_order = all_orders[count]
    count += 1

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict[to_find]
            add_list[-1] = amount
# End of loop

# Print ticket details
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')
#
# Create "Sub Total" column, fill with ticket and snack pricing
movie_frame["Sub Total"] = \
    movie_frame["Ticket"] + \
    movie_frame["Popcorn"] * price_dict["Popcorn"] + \
    movie_frame["Water"] * price_dict["Water"] + \
    movie_frame["Pita Chips"] * price_dict["Pita Chips"] + \
    movie_frame["M&Ms"] * price_dict["M&Ms"] + \
    movie_frame["Orange Juice"] * price_dict["Orange Juice"]

movie_frame["Surcharge"] = \
    movie_frame["Sub Total"] * movie_frame["Surcharge Multi"]

movie_frame["Total"] = movie_frame["Sub Total"] + \
    movie_frame["Surcharge"]

movie_frame = movie_frame.rename(columns={'Orange Juice': "OJ",
                                          'Pita Chips': "Chips"})

# Change pandas settings
pandas.set_option('display.max_columns', None)
pandas.set_option('precision', 2)

# Ask user if they wish to see extra info
print_all = input("Print all columns? (y) for yes: ")
if print_all == "y":
    print(movie_frame)
else:
    print(movie_frame[['Ticket', 'Sub Total', 'Surcharge', 'Total']])

print()

# Calculate ticket profit
profit = ticket_sales - (5 * tickets_sold)
print("Ticket profit: ${:.2f}".format(profit))


# Tell user if all tickets have been sold
if tickets_sold == max_tickets:
    print("You have sold all available tickets")
else:
    print("You have sold {} tickets".format(tickets_sold))
    print("{} seat(s) remain".format(max_tickets - tickets_sold))

