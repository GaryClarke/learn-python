# logical operators
# and - BOTH SIDES MUST EVALUATE TO TRUE
# print(x < 10 or not y <= 11)
# or - ONLY ONE SIDE MUST EVALUATE TO TRUE
# not - REVERSES THE BOOLEAN

x = 5
y = 10
a = x >= 5 and y % 2 == 0 # true
b = x // 2 == 3 or not y <= 9 # true
c = not x + y <= 15 and x % 4 <= 2 # false
print(a, b, c)




