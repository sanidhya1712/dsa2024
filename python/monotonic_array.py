def monotonic_array(array):
    if len(array)<=1:
        return True
    if array[0]<array[len(array)-1]:
        for i in range(len(array)-1):
            if array[i+1]<array[i]:
                return False
        return True
    else:
        for i in range(len(array)-1):
            if array[i+1]>array[i]:
                return False
        return True
    
print(monotonic_array([9,1,1,3,6]))