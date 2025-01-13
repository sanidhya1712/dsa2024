from hashlib import new
from typing import List


class Solution:
    '''unoptimized- my solution
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr2 = arr.copy()
        arr2.sort()
        # print(arr2)
        arrHash = {}
        rank = 1
        for i in range(len(arr)):
            if arr[i] in arrHash:
                arrHash[arr[i]].append(i)
            else:
                arrHash[arr[i]] = []
                arrHash[arr[i]].append(i)
        # print(arrHash)
        i = 0
        while i < len(arr2):
            srtList = arrHash[arr2[i]]
            srtLen = len(srtList)
            for j in range(srtLen):
                # print(x)
                arr[srtList[j]] = rank
            rank = rank+1
            i = i + srtLen
            # print(arr)
        return arr
    '''
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        num_to_rank = {}
        sorted_arr = sorted(arr)
        rank = 1
        for i in range(len(sorted_arr)):
            if i > 0 and sorted_arr[i] > sorted_arr[i - 1]:
                rank += 1
            num_to_rank[sorted_arr[i]] = rank
        for i in range(len(arr)):
            arr[i] = num_to_rank[arr[i]]
        return arr
    
        # Store the rank for each number in arr
        num_to_rank = {}
        # Deduplicate and sort arr
        nums = sorted(set(arr))
        print(nums)
        rank = 1
        for num in nums:
            num_to_rank[num] = rank
            rank += 1
        for i in range(len(arr)):
            arr[i] = num_to_rank[arr[i]]
        print(arr)
        return arr
            
        
a = Solution()
print(a.arrayRankTransform([40,20,30,10, 10]))