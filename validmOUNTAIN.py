def validMountain(arr):
    i = 1
    n = len(arr)
    while i < n and arr[i] > arr[i-1]:
        i += 1

    if i == n or i == 1:
        return False.

    while i < n and arr[i] < arr[i-1]:
        i += 1
    return i == n


arr = [1,2,3,4,5,6,7,6,5,4,3,2,1]
result = validMountain(arr)

print(arr, " is ",result)