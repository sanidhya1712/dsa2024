#Optimized sol
def isomorphic_strings(s, t):
    dict1 = {}
    if len(s)!=len(t):  return False
    for i in range(0,len(s)):
        if s[i] in dict1:
            if (dict1[s[i]]==t[i])== False:
                return False
        else:
            dict1[s[i]]=t[i]
    return True
print(isomorphic_strings('aabcba','zzthtr'))