def majorityElement(nums):
    dict_count = {}
    for i in range(len(nums)):
        if nums[i] in dict_count:
            dict_count[nums[i]] += 1
        else:
            dict_count[nums[i]] = 1
    for key, value in dict_count.items():
        if value > len(nums) // 2:
            return key
    return None
# optimal approach- Moore's Voting Algorithm
# Time complexity: O(n)
# Space complexity: O(1)
# Moore's Voting Algorithm
# 1. Initialize a count variable to 0 and a candidate variable to None.
# 2. Iterate through the array:
#    - If count is 0, set the candidate to the current element.
#    - If the current element is equal to the candidate, increment count.
#    - If the current element is not equal to the candidate, decrement count.
# 3. After the first pass, the candidate is the potential majority element.
# 4. Verify the candidate by counting its occurrences in the array.
# 5. If the count is greater than n/2, return the candidate; otherwise, return None.
def majorityElement(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    count = 0
    for num in nums:
        if num == candidate:
            count += 1
    if count > len(nums) // 2:
        return candidate
    return None
print(majorityElement([1, 2, 3, 2, 2, 4, 2, 5]))