# slicing lists
# revise index accessing
#          0  1  2  3  4
#         -5 -4 -3 -2 -1
# negative indices
# list[start:end]
# explain is non-inclusive
numbers = [0, 1, 2, 3, 4]
# [1:] open end / [:3] open start

# list[start:end:skip]
# print(numbers[1:-1:2]) odd numbers

# strings - show index, slices etc, get lastname
name = 'Gary Clarke'
#print(name[-6:-1:2])


# challenge
# create a function that will remove the file type from
# the name of a photo
# the function must be able to work on either
dog_picure = 'dog.jpg'
beach_picture = 'beach.png'

def remove_extension(filename):
    return filename[:-4]

photo_name = remove_extension(beach_picture)
print(photo_name)










