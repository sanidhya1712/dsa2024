/**
 * @param {number[]} cost
 * @return {number}
 */
var minCostClimbingStairs = function (a) {
    let start1 = a[0]
    let start2 = a[1]
    let start1Sum , start2Sum
    const arrLen = a.length
    if (arrLen<=3) {
        if (arrLen === 0) {
            return 0
        }else if (arrLen === 1) {
            return a[0]
        }else if (arrLen === 2) {
            if (a[0]>a[1]) {
                return a[1]
            }else{
                return a[0]
            }
        }else{
            start1Sum = (start1 + a[1]) < (start1 + a[2]) ? (start1 + a[1]) : (start1 + a[2])
            if (start1Sum<start2) {
                return start1Sum
            }else{
                return start2
            }
        }
    }else{
        start1Sum = (start1 + a[1]) < (start1 + a[2]) ? (start1 + a[1]) : (start1 + a[2])
        start2Sum = (start2 + a[2]) < (start2 + a[3]) ? (start2 + a[2]) : (start2 + a[3])
    }
    let start = start1Sum < start2Sum ? start1 : start2
    let startIndex = start1Sum < start2Sum ? 0 : 1
    let final = start
    while (true) {
        if ((startIndex + 2) === arrLen || (startIndex + 1) === arrLen) {
            return final
        }
        const v1 = a[startIndex + 1]
        const v2 = a[startIndex + 2]
        if (v1 < v2) {
            final = final + v1
            startIndex = startIndex + 1
        } else {
            final = final + v2
            startIndex = startIndex + 2
        }
    }
};

console.log(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]));