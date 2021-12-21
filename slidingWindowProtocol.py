# Brute force
# def sliding_window_protocol(arr, k):
#     max_sum = -9999
#     n = len(arr)
#     for i in range(n-k+1):
#         window_sum = 0
#         for j in range(k):
#             window_sum += arr[i + j]
#             max_sum = max(max_sum, window_sum)
#     return max_sum
#

# Optimized Solution

def sliding_window_protocol(arr, k):
    max_sum = sum([arr[i] for i in range(k)])
    n = len(arr)
    for i in range(n-k):
        window_sum = max_sum - arr[i] + arr[i + k]
        max_sum = max(window_sum, max_sum)
    return max_sum


if __name__ == "__main__":
    arr = [80, -50, 90, 100]
    k = 2
    result = sliding_window_protocol(arr, k)
    print("result: ", result)

