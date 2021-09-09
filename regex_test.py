import regex

strings = [
    "Popcorn",
    "2 pc",
    "1.5OJ",
    "4OJ"
]

for item in strings:
    number_regex = "^[1-9]"

    if regex.match(number_regex, item):
        amount = int(item[0])
        snack = item[1:]

    else:
        amount = 1
        snack = item

    snack = snack.strip()

    print("Amount:", amount)
    print("Snack:", snack)
    print("Length:", len(snack))