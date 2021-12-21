def maxChar(str):
    my_dic = {}
    for char in str:
        if char in my_dic.keys():
            val = my_dic[char]
            val += 1
            my_dic[char] = val
        else:
            my_dic[char] = 1

    print(max(my_dic, key=my_dic.get))


if __name__ == "__main__":
    maxChar(input("Enter a string....>>"))