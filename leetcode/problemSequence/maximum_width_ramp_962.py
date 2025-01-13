# Brute force, Unoptimized
'''var maxWidthRamp = function (nums) {
    let width = 0
    for (let i = 0; i < nums.length - 1; i++) {
        const element = nums[i];
        for (let j = i; j < nums.length; j++) {
            if (element <= nums[j]) {
                width = (j - i) > width ? j - i : width
            } else {
                continue
            }
        }

    }
    return width
};

console.log(maxWidthRamp([6, 0, 8, 2, 1, 5])) 
'''

from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        right_max = [None] * n

        # Fill right_max array with the maximum values from the right
        right_max[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], nums[i])

        left = 0
        right = 0
        max_width = 0

        # Traverse the array using left and right pointers
        while right < n:
            # Move left pointer forward if current left exceeds right_max
            while left < right and nums[left] > right_max[right]:
                left += 1
            max_width = max(max_width, right - left)
            right += 1

        return max_width
    
s = Solution()
print(s.maxWidthRamp([9,8,1,0,1,9,4,0,4,1]))