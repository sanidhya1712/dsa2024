"""Question

You are given an array of Integers in which each subsequent value is not less than the previous value. Write a function that takes this array as an input and returns a new array with the squares of each number sorted in ascending order."""
#brute force
# Time = O(nlogn)  Space = O(1)
"""def sorted_squared(array):
  #write code here.make sure to return desired array
    if len(array)==0:
        return []
    for i in range(0,len(array)):
        print(array[i])
        array[i]=array[i]*array[i]
    array=sorted(array)
    return array
"""
#Optimized solution
# Time = O(n) Space = O(n)
def sorted_squared(array):
  #write code here.make sure to return desired array
    if len(array)==0:
        return []
    new_array = [0] * len(array)
    j=0
    k=len(array)-1
    for i in range(len(array)-1,-1,-1):
        sqk = array[k]**2
        sqj = array[j]**2
        print(j, "   ", k)
        print(array, "  ", sqk, "   ", i, "   ", sqj, "   ",new_array)
        if sqk>sqj:
            new_array[i]= sqk
            k=k-1
        else:
            new_array[i]=sqj
            j=j+1
        print(j, "   ", k)
    print(new_array)
    return new_array
        

sorted_squared([-1, 0, 3, 5])