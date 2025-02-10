// For XOR, sequence doesn't matter, 0 XOR 0 = 0 and 1 XOR 1 = 0
var singleNumber = function (nums) {
    let result = 0;
    for (let num of nums) {
        result ^= num;
    }
    return result;
};

singleNumber([4, 1, 2, 1, 2])