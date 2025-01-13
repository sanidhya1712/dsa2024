from ast import List
# Brute force

class Solution:
    def smallestChair(self, times, targetFriend):
        target_time = times[targetFriend]
        times.sort()

        n = len(times)
        chair_time = [0] * n

        for time in times:
            for i in range(n):
                if chair_time[i] <= time[0]:
                    chair_time[i] = time[1]
                    if time == target_time:
                        return i
                    break
        return 0
    
s = Solution()
s.smallestChair([[3,10],[1,5],[2,6]], 0)