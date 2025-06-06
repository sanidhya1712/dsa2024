from typing import List

def maxProfit(arr: List[int]) -> int:
    maxPro = 0
    n = len(arr)


    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                maxPro = max(arr[j] - arr[i], maxPro)


    return maxPro
# optimal approach
def maxProfit(arr: List[int]) -> int:
    minPrice = arr[0]
    maxPro = 0
    n = len(arr)

    for i in range(1, n):
        cost = arr[i] - minPrice
        maxPro = max(cost, maxPro)
        minPrice = min(minPrice, arr[i])

    return maxPro
print(maxProfit([7, 1, 5, 3, 6, 4]))