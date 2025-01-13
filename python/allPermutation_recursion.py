def permute(nums):
        result = []
        n = len(nums)
        def backtrack(perm):
            if len(perm) == len(nums):
                result.append(perm.copy())
                return
            for i in range(n):
                if nums[i] in perm:
                    continue
                perm.append(nums[i])
                backtrack(perm)
                perm.pop()
        backtrack([])
        return result

print(permute([1,2,3]))