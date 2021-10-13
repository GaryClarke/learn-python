# knowledge check

# 1. calculate 10 cubed
# print(10 ** 3)

# 2. Use slicing to create a new version of this string with the
# '.tech' part removed
url = 'garyclarke.tech'
# print(url[:-5])

# 3. Use f-string interpolation to add your name to the end
# this string (not concatenation)
name = 'Gary'
phrase = f'Hello, my name is {name}'
# print(phrase)

# 4. REMOVE the value at index 2 from this list and store in
# a variable
my_list = ['Apple', 'Microsoft', 'Amazon', 'Google']
#removed_item = my_list.pop(2)

#5. Loop through my_list and print the index and value of each item
# for index, value in enumerate(my_list):
    # print(index, value)

#6. Access and store the value 'Python' from this nested
# data structure
info = {
    'software': ['VSCode', 'PyCharm'],
    'programming-languages': ['PHP', 'Python', 'JavaScript']
}
# print(info['programming-languages'][1])

#7. Covert this tuple into a list, store as my_list
my_tuple = ('gary', 'clarke', 'tech')
my_list = list(my_tuple)
# print(my_list)

#8. Unpack my_list into individual variables
gary, clarke, tech = my_list

#9. Write a function which lets you know if one number is
# exactly divisible by another it must return a boolean value
def is_divisible(num1, num2):
    return num1 % num2 == 0

# 10. which of these evaluates to true
bools_one = 9 % 4 > 2 or 100 not in range(1, 101)

bools_two = 1 + 3 ** 4 < 100 \
            and len(info['software']) not in {'a': 1, 2: 2, 'c': 3}


