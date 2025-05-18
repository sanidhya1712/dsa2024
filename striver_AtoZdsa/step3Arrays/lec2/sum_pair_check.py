def sum_pair_check(arr, k):
    dict = {}
    for i in range(len(arr)):
        if k-arr[i] in dict:
            print("Pair found:", arr[i], k-arr[i])
            return True
        dict[arr[i]] = i
    return False
# Two pointer approach  
def sum_pair_check(arr, k):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] + arr[right]==k:
            print("Pair found:", arr[left], arr[right])
            return True
        elif arr[left] + arr[right] < k:
            left += 1
        else:
            right -= 1
    print("No pair found")  
    return False
print(sum_pair_check([1, 2, 3, 4, 5], 6))