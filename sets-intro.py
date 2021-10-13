# sets - unordered / unindexed collection of UNIQUE elements

# create a set
my_set = set()
my_set.add(10)
my_set.add(5)

# add items to the set

my_list = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7]
evens = set()
odds = set()

# challenge - loop over my_list
    # IF the number is even, add to evens
    # ELSE, add to odds
for num in my_list:
    if num % 2 == 0:
        evens.add(num)
    else:
        odds.add(num)

print(set(my_list))











