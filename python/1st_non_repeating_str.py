#Optimized sol
def non_repeating_char(str):
    hashDic = {}
    for value in str:
        print(value)
        if value in hashDic:
            hashDic[value]+=1
        else:
            hashDic[value]=1
    for i in range(len(str)):
        if hashDic[str[i]]==1:
            return i
    return None
print(non_repeating_char('a123412a'))