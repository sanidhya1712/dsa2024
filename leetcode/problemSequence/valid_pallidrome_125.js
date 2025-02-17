/**
 * @param {string} s
 * @return {boolean}
 */

/* Brute force taking extra space, can optimize this
with iterating over original string and using continue whenever encountering
special character
*/
var isPalindrome = function (s) {
    str = ''
    for (const val of s) {
        console.log(val.charCodeAt(0));

        if ((val.charCodeAt(0) >= 65 && val.charCodeAt(0) < 91) || (val.charCodeAt(0) >= 97 && val.charCodeAt(0) < 123) || (val.charCodeAt(0) >= 48 && val.charCodeAt(0) < 58)) {
            str = str + val.toLowerCase()
        }
    }
    console.log(str);
    if (str.length < 2) {
        return true
    } else {
        let n = 0, m = str.length - 1
        console.log(n, m);
        flag = true
        while (m > n) {
            if (str[n] != str[m]) {
                return false
            } else {
                n++
                m--
            }
        }
        return flag
    }
};

console.log(isPalindrome("9P"));
