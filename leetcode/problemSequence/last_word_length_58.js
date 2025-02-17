/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function (s) {
    strArr = s.split(' ')
    console.log(strArr);
    for (let i = strArr.length - 1; i >= 0; i--) {
        if (strArr[i].length > 0) {
            return strArr[i].length
        }
    }
    return ""
};

console.log(lengthOfLastWord("   fly me   to   the moon  "));
