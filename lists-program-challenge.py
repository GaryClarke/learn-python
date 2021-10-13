star_ratings = [4, 2, 3, 5, 4, 1, 3, 4, 5, 1, 3]
# 1. Using an input function, ask the user to
# enter a star rating (1 - 5)
# 2. Store the user input value in a variable
user_rating = int(input('Please enter a star rating (1-5): '))
# 3. Append the rating to the star_ratings list
star_ratings.append(user_rating)
# 4. Calculate the average of the LAST 5 ratings in star_ratings
last_5 = star_ratings[-5:]
# 5. Store this in a variable
average_rating = sum(last_5) / len(last_5)
# 6. Print the value to the console / terminal
print(average_rating)
# 7. Test your work
# 8. Fix any errors (debug) in your code