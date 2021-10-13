# dictionary methods
my_dict = {'a': 100, 'b': 200, 'c': 300}

# check for value in dictionary

# demonstrate that keys are used by default (in, for, list)

# order is preserved

# show how to get values (in, for, list)

# ITERABLE OBJECTS
# print my_dict.values()

# print my_dict.keys()

# my_dict.items() challenge - convert to a list -
# what TYPE are the individual items
# for key, value in my_dict.items():
#     print(key, value)

# remove items from a dictionary (del, pop)

popped_item = my_dict.pop('b')
print(popped_item, my_dict)

# dict.keys() returns an iterable object,
# not a list-like object.
# It will work anywhere an iterable will work
# -- not any place a list will. a list is also an iterable,
# but an iterable is NOT a list (or sequence...)