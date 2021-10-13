# strings roundup
# split string over lines using \
text = "Sed ut perspiciatis unde omnis iste natus error " \
    "sit voluptatem accusantium doloremque laudantium, " \
    "totam rem aperiam, eaque ipsa quae ab illo inventore " \
    "veritatis et quasi architecto beatae `vitae dicta sunt explicabo."

# split f string over lines using \
new_text = f"Sed ut perspiciatis unde omnis iste natus error " \
    f"sit voluptatem accusantium doloremque laudantium"

# using ''' to format string
text = '''
Sed ut perspiciatis unde omnis iste natus error sit 
voluptatem accusantium doloremque laudantium, totam rem aperiam, 
eaque ipsa quae ab illo inventore veritatis et quasi architecto 
beatae vitae dicta sunt explicabo.
'''
# concatenation
name = 'Gary ' + 'Clarke'

# concatenating numbers as strings
sum = '5' + '4'

# muliplying characters
phrase = '_' * 5

# immutability
# print(name)

# split a string on spaces and other chars
phrase = 'Ben, Mike, Jerry'
# print(phrase.split(', '))

# reversing a string
mike = phrase[::-1]
print(mike)








