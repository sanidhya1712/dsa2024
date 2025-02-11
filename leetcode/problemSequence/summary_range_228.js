/**
 * @param {number[]} nums
 * @return {string[]}
 */
var summaryRanges = function (nums) {
    start = nums[0]
    result = []
    for (let i = 1; i <= nums.length; i++) {
        console.log(i, nums[i]);

        if (nums[i] - nums[i - 1] == 1) continue
        if (start == nums[i - 1]) {
            result.push(`${start}`)
        } else {
            result.push(`${start}->${nums[i - 1]}`)
        }
        start = nums[i]
    }
    return result
};

console.log(summaryRanges([0, 2, 3, 4, 6, 8, 9]))