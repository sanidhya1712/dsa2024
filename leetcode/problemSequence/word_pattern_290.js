/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */
var wordPattern = function (pattern, s) {
    str = s.split(" ")
    res = {}
    if (str.length != pattern.length) return false
    console.log(str);
    for (const i in pattern) {
        if (pattern[i] in res) {
            if (res[pattern[i]] != str[i]) {
                return false
            }
        } else {
            if (Object.values(res).includes(str[i])) {
                return false
            }
            res[pattern[i]] = str[i]
        }
    }
    return true
};

console.log(wordPattern("abba", "dog dog dog dog"));
