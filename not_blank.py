# Define function
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response

        else:
            print("Please enter your name, it can't be blank.")


# Run the function

name = not_blank("Please enter your name: ")