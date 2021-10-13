fares = {
    'student': 0,
    'junior': 10,
    'adult': 20,
    'senior': 5
}

passenger = {
    'name': 'Jackson Clarke',
    'age': 67,
    'is_student': False
}

student_passenger = {
    'name': 'Mark Zuckerberg',
    'age': 22,
    'is_student': True
}

# Write a conditional to check whether the passenger is under 18
# IF they are under 18, print a junior fare
# if passenger['age'] < 18:
#     print(fares['junior'])
# # ELSE print senior fare
# else:
#     print(fares['adult'])
# NO HARDCODING VALUES - print the values from the dictionary



# create a function called get_fare
# it will take 2 inputs: passenger and fares
def get_fare(passenger, fares):
    if passenger['is_student']:
        return fares['student']
    elif passenger['age'] < 18:
        return fares['junior']
    elif passenger['age'] < 65:
        return fares['adult']
    else:
        return fares['senior']

# return the value instead of printing it
# call the function in your code
# print the returned value
passenger_fare = get_fare(passenger, fares)

print(passenger_fare)












