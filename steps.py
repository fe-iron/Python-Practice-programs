num = int(input("Enter the limit of the steps.."))
pounds = ""
for i in range(1, num+1):
    pounds += "'" + "#"*i + " " * (num-i) + "'"
    pounds += "\n"

print(str(pounds))