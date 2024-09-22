"""def k_rotate_array(array, k):
    if len(array)<=1:
        return array
    k=abs(k%len(array))
    for i in range(k):
        print(array[len(array)-1:],"   ",array[0:len(array)-1])
        array = array[len(array)-1:]+array[0:len(array)-1]
    return array"""
#optimum sol
def reverse(array,start,end):
    while(start<end):
        array[start],array[end] = array[end], array[start]
        start +=1
        end -=1
    return array

def k_rotate_array(array,k):
    if len(array) == 0: return []
    k= k % len(array)
    reverse(array, 0, len(array)-1)
    reverse(array, 0, k-1)
    reverse(array, k, len(array)-1)
    return array  
print(k_rotate_array([9,1,1,3,6], 9))