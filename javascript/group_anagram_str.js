const group_anagrams = (strings)=>{
    //write your code here
    finalArr = []
    dictFinal = {}
    for (i of strings){
        console.log(i)
        x = i.split("").sort().join("")
        console.log(x)
        if (x in dictFinal)
            dictFinal[x].push(i)
        else
        dictFinal[x] = [i]
    }
    for (i in dictFinal)
        finalArr.push(dictFinal[i])

    return finalArr
}


console.log(group_anagrams(['abc', 'cat', 'cab', 'atc']))