/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function (s) {
    obj = {}
    index = -1
    for (const i in s) {
        if (s[i] in obj) {
            obj[s[i]].push(Number(i))
        } else {
            obj[s[i]] = [Number(i)]
        }
    }
    for (const key in obj) {
        if (obj[key].length === 1) {
            if (index < 0) index = obj[key][0]
            if (obj[key][0] < index) index = obj[key[0]]
        }
    }
    return index
};

console.log(firstUniqChar('leetcode'));
