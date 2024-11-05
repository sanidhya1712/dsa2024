/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
    if (s.length <= 1) {
        return false
    }
    if (['(', '{', '['].includes(s[s.length - 1]) || [')', '}', ']'].includes(s[0])) {
        return false
    }
    stack = []
    mapping = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    for (const c of s) {
        if (Object.values(mapping).includes(c)) {
            stack.push(c);
        } else if (mapping.hasOwnProperty(c)) {
            if (!stack.length || mapping[c] !== stack.pop()) {
                return false;
            }
        }
    }
    return stack.length === 0
};

console.log(isValid(')([])'))