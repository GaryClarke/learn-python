# modulo
# odds / evens example

# floor
# weeks in year example
weeks_in_year = 366 // 7

# challenge
evens = list()
odds = list()
# write a for loop which loops over numbers 1 - 100
for number in range(1, 101):
# using what just learnt...
# APPEND even numbers to evens list
    if number % 2 == 0:
        evens.append(number)
# append odd numbers to odds list
    else:
        odds.append(number)

# print odds and evens lists
print('Odds: ', odds)
print('Evens: ', evens)









