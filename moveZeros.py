# Brute Force
# def move_zeros(nums):
#     for ele in nums:
#         if ele == 0:
#             nums.remove(0)
#             nums.append(0)
#     return nums

# Optimized Approach

def move_zeros(num):
    j = 0
    n = len(num)
    for i in num:
        if i != 0:
            num[j] = i
            j += 1

    for x in range(j, n):
        num[x] = 0
    return nums


if __name__ == '__main__':
    nums = [1, 3, 40, 4, 40, 5, 6, 0, 6, 6, 0, 7, 8, 99, 0]
    print("Expected Output: ", move_zeros(nums))