# Imports

# Functions
def not_blank(question, error):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response

        else:
            print(error)


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


# Variables
name = ""
tickets_sold = 0
ticket_price = 0
profit = 0
max_tickets = 5  # Will be 150 for final version
loop = True
# Main Routine

# Set up dictionaries / lists

# Ask user if they've used the program before

# Loop code for ticket details

while loop:

    while name != "quit" and tickets_sold < max_tickets:

        # Ask for name (can't be blank)
        name = not_blank("Please enter your name or type quit to stop booking seats: ",
                         "Please enter your name or quit, this can't be blank.\n")
        if name == "quit":
            loop = False
            break
        # Ask for age (12 - 130)

        age = int_check("How old are you? ")

        if age < 12:
            print("You are too young for this movie, sorry")
        elif age > 130:
            print("Are you sure that you're {} years old? That looks like a mistake.".format(age))
        else:

            if age < 16:
                ticket_price = 7.50

            elif age >= 65:
                ticket_price = 6.50

            else:
                ticket_price = 10.50

            print("That'll be ${:.2f} total".format(ticket_price))
            print("Here's your ticket, enjoy the movie")
            tickets_sold += 1
            profit += ticket_price - 5

        print("There are {} seats left\n".format(max_tickets - tickets_sold))

        # Added to see when the loop has ended, will change places as code develops
if tickets_sold == max_tickets:
    print("All tickets have been sold, there are no more seats available")
    print("The total profit earned is ${:.2f}".format(profit))
else:
    print("{} tickets have been sold, there are {} seats available".format(tickets_sold, max_tickets - tickets_sold))
    print("The total profit earned is ${:.2f}".format(profit))

    # Calculate ticket prices

    # Loop to ask for snacks

    # Calculate snack prices

    # Ask for payment (apply 5% surcharge if credit card)

# Calculate total ticket and snack cost

# Save to a text / csv file
