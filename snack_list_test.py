import pandas
# Initialise snack lists

all_names = ['Medic', 'Engineer', 'Pyro', 'Spy', 'Heavy']

popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

movie_data_dict = {
    'Name': all_names,
    'Popcorn': popcorn,
    'Water': water,
    "Pita Chips": pita_chips,
    'M&Ms': mms,
    'Orange Juice': orange_juice
}

test_data = [
    [[2, 'Popcorn'], [1, "M&Ms"]],
    [[4, 'Water']],
    [[3, 'Pita Chips'], [2, 'M&Ms'], [3, 'Orange Juice']],
    [[]],
    [[2, 'Popcorn'], [3, 'Water'], [1, 'Pita Chips'], [4, 'M&Ms']]
]

count = 0
for client_order in test_data:
    # Assume no snacks have been ordered
    for item in snack_lists:
        item.append(0)

    # print(snack_lists)

    # Get orders (hard coded for testing)
    snack_order = test_data[count]
    count += 1

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict[to_find]
            add_list[-1] = amount

print()
print(f"Names: {all_names}")
print(f"Popcorn: {snack_lists[0]}")
print(f"M&MS: {snack_lists[1]}")
print(f"Pita Chips: {snack_lists[2]}")
print(f"Water: {snack_lists[3]}")
print(f"Orange Juice: {snack_lists[4]}")

movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')
print(movie_frame)