# explain what functions are

# show how to create own function
def say_hello(first_name):
    print('Hello ' + first_name)


# say_hello('Gary')

# explain difference between print() and others
first_name = 'Gary'
name_length = len(first_name)


# print(name_length)
# create a square function which returns a value
def square_number(number):
    squared_number = number ** 2
    return squared_number


# call, store and print
squared = square_number(3)
# print(squared)

# explain more than one input permitted
def add(a, b):
    c = a + b
    return c

sum = add(4, 5)
sum2 = add(6, 7)
print(sum)
print(sum2)










