from ast import List


class Solution:
    def moveZeroes(self, nums) -> None:
        start = 0
        for i in nums:
            if i != 0:
                nums[start] = i
                start+=1
        for i in range(start,len(nums)):
            nums[i] = 0
        print(nums)
s = Solution()
s.moveZeroes([0,1,0,3,12])