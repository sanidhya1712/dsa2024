/**
 * @param {string} s
 * @return {number}
 */
var minAddToMakeValid = function (s) {
    openBracket = []
    closeBracket = 0
    for (const x of s) {
        if (x === '(') {
            openBracket.push(x)
        } else {
            if (openBracket.length > 0) {
                openBracket.pop()
            } else {
                closeBracket = closeBracket + 1
            }
        }
    }
    return openBracket.length + closeBracket
};

console.log(minAddToMakeValid('()))'))