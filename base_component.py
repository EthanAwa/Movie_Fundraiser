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


# Variables
name = ""
count = 0
max_tickets = 5  # Will be 150 for final version

# Main Routine

# Set up dictionaries / lists

# Ask user if they've used the program before

# Loop code for ticket details
while name != "quit" and count < max_tickets:
    print("There are {} seats left".format(max_tickets - count))

    # Ask for name (can't be blank)
    name = not_blank("Please enter your name or type quit to stop booking seats: ",
                     "Please enter your name or quit, this can't be blank.\n")
    if name != "quit":
        count += 1
    print()

# Added to see when the loop has ended, will change places as code develops
if count == max_tickets:
    print("All tickets have been sold, there are no more seats available")
else:
    print("{} tickets have been sold, there are {} seats available".format(count, max_tickets - count))

    # Ask for age (12 - 130)

    # Calculate ticket prices

    # Loop to ask for snacks

    # Calculate snack prices

    # Ask for payment (apply 5% surcharge if credit card)

# Calculate total ticket and snack cost

# Save to a text / csv file
