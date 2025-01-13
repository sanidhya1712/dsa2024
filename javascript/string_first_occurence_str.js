var strStr = function (haystack, needle) {
    if (haystack.length < needle.length) {
        return -1;
    }

    for (let i = 0; i <= haystack.length - needle.length; i++) {
        console.log(haystack[i, i+ needle.length]);
        
        if (haystack.substring(i, i + needle.length) === needle) {
            return i;
        }
    }

    return -1;
};
// // smaller solution
// var strStr = function (haystack, needle) {
//     return haystack.indexOf(needle)
// };

console.log(strStr("sadbutsad", "sad"))