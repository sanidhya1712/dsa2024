// Optimized sol
const isomorphic_strings = (s, t) => {
    let dict1 = {}
    if (s.length != t.length) return false
    for (const i in s) {
        console.log(dict1, "s ---- ", s[i]);
        console.log(Object.keys(dict1).includes(s[i]), "---s[i] in Object.keys(dict1)---", s[i] in Object.keys(dict1));
        if (Object.keys(dict1).includes(s[i])) {
            console.log(t[i], "--dict --", dict1);
            if (!(dict1[s[i]] === t[i])) {
                return false
            }
        } else {
            dict1[s[i]] = t[i]
        }
    }
    return true
}
console.log(isomorphic_strings('aabcba', 'zzthtr'))