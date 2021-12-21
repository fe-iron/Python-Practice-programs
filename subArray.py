def sub_array(arr, size):
    new_arr = []
    whole_arr = []
    count = 0
    i = 0
    for ele in arr:
        i += 1
        if count < int(size):
            new_arr.append(ele)
            count += 1
        else:
            whole_arr.append(new_arr)
            new_arr = []
            count = 1
            new_arr.append(ele)
        if len(arr) == i:
            whole_arr.append(new_arr)

    print(whole_arr)


if __name__ == "__main__":
    arr = input("Enter an Array of Integers.. ")
    arr = arr.split(" ")
    if arr[-1] == " ":
        arr.pop()
        print(arr)
    size = input("Enter the size.. ")
    sub_array(arr, size)
