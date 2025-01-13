"""def max_area(array):
    area_max = 0
    if len(array)<=1: 
        return area_max
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            area = min(array[i], array[j])*(j-i)
            area_max= max(area,area_max)
    return area_max"""

#Optimized sol
#Always move pointer on lower value as height cannot increase if we move the pointer at higher value
def max_area(array):
    left = 0
    right = len(array)-1
    max_area=0
    while(left<right):
        area = min(array[left], array[right]) * (right - left)
        max_area = max(area,max_area)
        if array[left]<array[right]:
            left +=1
        else:
            right -= 1
    return max_area
print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))