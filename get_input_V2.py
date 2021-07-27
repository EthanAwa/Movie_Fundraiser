# get_input_V2 function

# Variables
name = ""
count = 0
max_tickets = 5

# Looping code
# If the user doesn't enter quit and tickets sold < 5, continue looping
while name != "quit" and count < max_tickets:
    print("There are {} seats left".format(max_tickets - count))

    # Get user's name
    name = input("Name: ")
    if name != "quit":
        count += 1
    print()

# Check if all tickets have been sold, and print feedback based on results
if count == max_tickets:
    print("All tickets have been sold, there are no more seats available")
else:
    print("{} tickets have been sold, there are {} seats available".format(count, max_tickets - count))