/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
    x = x.toString()
    let mid = Math.floor((x.length) / 2)
    for (let i = 0; i <= mid; i++) {
        if (x[i] != x[x.length - i - 1]) {
            return false
        }
    }
    return true
};

console.log(isPalindrome(1221))