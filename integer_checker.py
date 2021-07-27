def int_check(question):
    error = "Please enter a whole number that is more than 0\n"

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
                  "or a word (e.g Three)\n")


int_check("Please enter a whole number that is more than 0: ")