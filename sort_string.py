'''
    Author: Faiz Elahi
    github Profile: https://github.com/fe-iron
    LinkedIn Profile: https://www.linkedin.com/in/faiz-elahi-13204b132/
    Python | Django Developer
'''

num_in_string = input("Enter a numbers saparated by commas ")
num_list_string = num_in_string.split(",")

num_in_list = []

for element in num_list_string:
    if element == " ":
        pass
    elif element == ",":
        pass
    else:
        num_in_list.append(int(element))

num_in_list.sort()
num_in_string = ","
varName = 12
num_in_string = num_in_string.join(str(i) for i in num_in_list)

print(num_in_string)
