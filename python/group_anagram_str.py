def group_anagrams(strings):
    #write your code here
    finalArr = []
    dictFinal = {}
    for i in range(len(strings)):
        print(strings[i])
        x=sorted(strings[i])
        x= ''.join(x)
        print(x)
        if x in dictFinal:
            dictFinal[x].append(strings[i])
        else:
            dictFinal[x] = [strings[i]]
    for i in dictFinal:
        finalArr.append(dictFinal[i])
     
    return finalArr
      
    
print(group_anagrams(['abc','cat', 'cab', 'atc']))