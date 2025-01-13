// Optimized sol
const two_sum = (array, target) => {
    dict1 = {}
    for (i in array) {
        // console.log(i);
        if (target - array[i] in dict1) {
            return [i, dict1[target - array[i]]]
        }
        else {
            dict1[array[i]] = i
        }
    }
    // for (i in dict1) {
    //     // console.log(i);
    //     if (target - array[i] in dict1) {
    //         return [i, dict1[target - array[i]]]
    //     }
    //     else {
    //         dict1[array[i]] = i
    //     }
    // }
    return []
}

console.log(two_sum([1, 8, 6, 2, 5, 4, 8, 3, 7], 13))