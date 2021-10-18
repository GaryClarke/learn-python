import csv

classes = {1: {}, 2: {}, 3: {}, 4: {}, 5: {}}

with open('students.csv') as students_file:
    reader = csv.reader(students_file)
    for index, name in reader:
        id = int(index)
        class_number = id % 5 + 1
        classes[class_number][id] = name

# write the names of each class's students
# to a txt file for that class

# 1. We will need a for loop which iterates over classes dict ITEMS
for class_number, cohort in classes.items():
    # 2. Use the class number to create a classname.txt filename
    # e.g. class1.txt
    filename = f'class{class_number}.txt'
    # 3. Loop over the student names
    for name in cohort.values():
        # 4. Open class<number>.txt for appending as class_file
        with open(filename, 'a') as class_file:
            # 5. Write the students name to the file
            class_file.write(f'{name}\n')

# 6. Check your folder for the created files (should be 5)




