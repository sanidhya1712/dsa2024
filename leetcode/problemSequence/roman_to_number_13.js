var romanToInt = function (s) {
    const sym = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    num = 0
    for (let i = 0; i < s.length; i++) {
        curr = sym[s[i]]
        next = sym[s[i + 1]]
        if (curr < next) {
            num += (next - curr)
            i++
        } else {
            num += curr
        }

    }
    return num
};

console.log(romanToInt("MCMXCIV"));
