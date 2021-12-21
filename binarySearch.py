bst_list = input("Enter the list in ascending order ").split(" ")
target = int(input("Enter number you want to search "))

def binary_search(bst_list, target):
    start = 0
    end = len(bst_list) - 1
    while start <= end:
        mid = (start + end) // 2

        if int(bst_list[mid]) == target:
            return mid
        elif int(bst_list[mid]) <= target:
            start += 1
        elif int(bst_list[mid]) >= target:
            end -= 1
    return 0


result = binary_search(bst_list, target)

if result:
    print(f"The {target} is present at {result}")