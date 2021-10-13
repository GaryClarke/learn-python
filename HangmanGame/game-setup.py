# ============= Game setup ===================
# 1. player A enter a phrase
# convert the phrase into blanked out version using underscores
    # (must be matching in length - must include spaces)
# 2. display blanked out version

phrase = input('[Player A] Please enter a phrase to solve: ')

enumerate_object = enumerate(phrase)
new_phrase = '_' * len(phrase)
letters_list = list(new_phrase)

for index, letter in enumerate(phrase):
    if letter == ' ':
        letters_list[index] = ' '

new_phrase = ''.join(letters_list)
print(new_phrase)


