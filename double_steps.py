import math
num = int(input("Enter the limit of the steps.."))
pounds = ""
for row in range(0, num):
    midpoint = math.floor((2*num - 1)/2)
    # pounds += "'" + "#"*i + " " * (num-i) + "'"
    for col in range(0, num*2-1):
        if midpoint - row <= col and midpoint + row >= col:
            pounds += "#"
        else:
            pounds += " "
    pounds += "\n"

print(pounds)