# nested data
# create mixed nested data e.g. lists, dictionaries
user_groups = [
    [
        {'name': 'Person A', 'is_student': True},
        {'name': 'Person B', 'is_student': False},
    ],
    [
        {'name': 'Person C', 'is_student': False},
        {'name': 'Person D', 'is_student': True},
    ]
]

# loop through the data and print some info reagrding the items
for user_group in user_groups:
    for user in user_group:
        if user['is_student']:
            print(f'{user["name"]} is a student')
        else:
            print(f'{user["name"]} is not a student')






