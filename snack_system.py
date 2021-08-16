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
        print("Invalid choice")

# List of all valid snacks and possible abbreviations
valid_snacks = [
    ["popcorn", "p", "corn"],
    ["M&M's", "mms", "m&ms", "m"],
    ["pita chips", "chips", "pc", "c"],
    ["water", "w"],
    ["orange juice", "oj", "juice"]
]

# Variables

snack_ok = ""
snack = ""

# Loop for easier testing
# for item in range(0,3):
#
#     desired_snack = input("Snack: ").lower()
#
#     for var_list in valid_snacks:
#
#         if desired_snack in var_list:
#
#             # Get snack name
#             snack = var_list[0].title()
#             snack_ok = "yes"
#             break
#
#         else:
#             snack_ok = "no"
#
#     if snack_ok == "yes":
#         print("Snack choice: ", snack)
#     else:
#         print("Invalid choice")
