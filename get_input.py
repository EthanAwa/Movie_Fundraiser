# get_input_V1 function
name = ""
count = 0
max_tickets = 5

# If the user doesn't enter quit and tickets sold < 5, continue looping
while name != "quit" and count < max_tickets:
    name = input("Name: ")
    count += 1
