def boatToSavePeople(people, limit):
    left = 0
    right = len(people) - 1
    noOfBoat = 0

    while left <= right:
        if left == right:
            print("Stored: ",people[right])
            left += 1
            noOfBoat += 1
            break
        if people[left] + people[right] <= limit:
            print("Stored: ", people[left], " ",people[right])
            left += 1
            right -= 1
            noOfBoat += 1
        else:
            print("Stored: ", people[right])
            right -= 1
            noOfBoat += 1

    return noOfBoat


people = [3, 2, 2, 1]
people.sort()
print(people)
limit = 3
result = boatToSavePeople(people, limit)
print(result)