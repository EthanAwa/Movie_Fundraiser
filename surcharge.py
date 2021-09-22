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


pay_method = [
    ["credit", "cr"],
    ["cash", "ca"]
]

name = ""
while name != "quit":
    name = input("Name: ")
    if name == "quit":
        break

    how_pay = "invalid choice"
    while how_pay == "invalid choice":
        how_pay = input("Please choose a payment method (cash or credit): ").lower()
        how_pay = string_check(how_pay, pay_method)

    subtotal = float(input("Sub total: $"))
    how_pay = how_pay.lower()
    if how_pay == "credit" or how_pay == "cr":
        surcharge = 0.05 * subtotal
    else:
        surcharge = 0

    total = surcharge + subtotal

    print("Name: {} | Subtotal: ${:.2f} | Surcharge: ${:.2f} | Total: ${:.2f}".format(name, subtotal, surcharge, total))

