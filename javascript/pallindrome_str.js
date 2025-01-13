//Optimal
// function is_palindrome(string){
//     const hashTable = {};
//     for(let i=0;i<string.length;i++){
//         if(string[i] in hashTable){
//             hashTable[string[i]]++;
//         } else{
//             hashTable[string[i]]=1;
//         }
//     }
//     for(let i=0;i<string.length;i++){
//         if(hashTable[string[i]]===1){
//             return i;
//         }
//     }
//     return null;
// }

//brute force
function is_palindrome(string){
    let palindrome = true;
    let i = 0
    let j = string.length-1
    if (string.length%2 === 0) {
        console.log("even");
        while (i<j) {
            console.log(i,"  ",j);
           if (string[i]===string[j]) {                
                i++
                j--
           }else{
                palindrome = false
                break
           } 
        }
    } else {
        console.log("odd");
        while (i<=j) {
            console.log(i,"  ",j);
            if (string[i]===string[j]) {                
                 i++
                 j--
            }else{
                 palindrome = false
                 break
            } 
         }
    }
    return palindrome
}
a='a12421a';
console.log(is_palindrome(a));