/**
 * @param {string} sentence1
 * @param {string} sentence2
 * @return {boolean}
 */

/* check if the sentences are similar by matching words from the beginning (prefix) and the end (suffix). 
If all words at the start and end match, the remaining words in the middle can be ignored, 
making the sentences similar. 
*/

// Assumption that sentence2 is bigger than sentence1
var areSentencesSimilar = function (sentence1, sentence2) {
    s1 = sentence1.split(" ")
    s2 = sentence2.split(" ")
    let [start, end1, end2] = [0, s1.length - 1, s2.length - 1]
    if (end1 > end2) {
        // if sentence1 is bigger than sentence2
        return areSentencesSimilar(sentence2, sentence1)
    }
    while (start < s1.length && s1[start] === s2[start]) {
        start += 1
    }
    while (end1 > 0 && s1[end1] === s2[end2]) {
        end1 -= 1
        end2 -= 1
    }
    console.log(start, end1, end2);

    return end1 < start
};

console.log(areSentencesSimilar("My Haley is don", "My Haley"))