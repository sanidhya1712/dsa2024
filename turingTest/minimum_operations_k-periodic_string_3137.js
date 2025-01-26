/**
 * @param {string} word
 * @param {number} k
 * @return {number}
 */
var minimumOperationsToMakeKPeriodic = function (word, k) {
    let s = new Map()
    for (let i = 0; i < word.length; i += k) {
        let c = word.slice(i, i + k)
        console.log(i);
        s.set(c, 1 + (s.get(c) || 0))
    }
    console.log(s.values());

    return Math.floor(word.length / k) - Math.max(...s.values())
};

console.log(minimumOperationsToMakeKPeriodic("leetcoleet", 2));
