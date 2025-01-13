// Optimized sol
const powerSum=(array,power=1)=>{
    let sum = 0
    for (const i in array) {
        if (Array.isArray(array[i])) {
            sum = sum + powerSum(array[i],power+1)
        }else{
            sum = sum + array[i]
        }
    }
    return Math.pow(sum,power);
}
console.log(powerSum([1,2,[7,[3,4],2]]));