def leaderArray(arr, n):
    ans = []
  
    for i in range(n):
        leader = True

        # Checking whether arr[i] is greater than all 
        # the elements in its right side
        for j in range(i+1, n):
            if arr[j] > arr[i]:
                # If any element found is greater than current leader,
                # curr element is not the leader.
                leader = False
                break

        # Push all the leaders in ans array.
        if leader:
            ans.append(arr[i])

    return ans
# optimal approach
def leaderArray(arr):
    max = arr[-1]
    leaders = [max]
    for i in range(len(arr)-1,-1, -1):
        if arr[i]>max:
            max= arr[i]
            leaders.append(max)
    leaders.reverse()
    return leaders
        
print(leaderArray([7, 1, 5, 3, 6, 4]))