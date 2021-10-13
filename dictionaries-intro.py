# limitation of lists
# user = [
#     'Gary',
#     'Clarke',
#     '22 Acacia Avenue, London, UK',
#     'GBP',
#     44123456789
# ]
# create a dictionary {k:v}
user = {
    'first_name': 'Gary',
    'last_name': 'Clarke',
    'address': {
        'street_address': '22 Acacia Avenue',
        'city': 'London',
        'country': 'UK'
    },
    'currency': 'GBP',
    'phone': 44123456789
}
# print dictionary
# access an item in dictionary
# explain data types
user['phone'] = 333
# print(user)
# add a new key to existing
# update a value in existing
# show dictionary method(s)
print(user.values())








