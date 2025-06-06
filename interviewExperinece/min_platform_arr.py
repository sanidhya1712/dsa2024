#Optimized solution by not checking individual but clubbing all arrival and departure in sequence
def calculateMinPatforms(at, dt, n):
    at.sort()
    dt.sort()
    print(at, dt)
    i, j = 0, 0
    count , maxCount = 0, 0
    while i < n and j< n:
        if at[i]<= dt[j]:
            count+=1
            i+=1
        else:
            count-=1
            j+=1
        maxCount = max(maxCount,count)
    return maxCount

print(calculateMinPatforms( [900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000], 6))