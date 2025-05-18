def unionSortedArray(arr1, arr2):
    # Create a set to store unique elements
    # and a list to store the union
    s = set()
    union = []
    
    for num in arr1:
        s.add(num)
    
    for num in arr2:
        s.add(num)
    for num in s:
        union.append(num)
    
    return union
    # # Merge two sorted arrays
    # i = 0
    # j = 0
    # ans = []
    # # Check for duplicates
    # while i < len(arr1) and j < len(arr2):
    #     if arr1[i] < arr2[j]:
    #         ans.append(arr1[i])
    #         i += 1
    #     elif arr1[i] > arr2[j]:
    #         ans.append(arr2[j])
    #         j += 1
    #     else:
    #         ans.append(arr1[i])
    #         i += 1
    #         j += 1
    # return ans
print(unionSortedArray([1,2,3,4,5,6,7,8,9,10],[2,3,4,4,5,11,12]))