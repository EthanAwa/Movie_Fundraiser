# not_blank Function V2
# Define function
def not_blank(question, error):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response

        else:
            print(error)


# Run the function

name = not_blank("Please enter your name: ",
                 "Please enter your name, it can't be blank.")
print("Hello, {}".format(name))

