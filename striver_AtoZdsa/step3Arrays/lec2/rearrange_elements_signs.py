def rearrange_elements_signs(arr):
    a = []
    b = []
    c = []
    for i in arr:
        if i<0:
            b.append(i)
        else:
            a.append(i)
    i = 0
    while i < len(a):
        c.append(a[i])
        c.append(b[i])
        i+=1
    return c

# Optimal approach
def rearrange_elements_signs(arr):
    a = [0] * len(arr)
    pos, neg = 0, 1
    for i in arr:
        if i<0:
            a[neg] = i
            neg +=2
        else:
            a[pos] = i
            pos+=2
    return a
print(rearrange_elements_signs([-1, 2, -3, 4, -5, 6]))