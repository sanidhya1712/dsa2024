/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var nextGreaterElement = function (nums1, nums2) {
    let finalList = []
    for (let i = 0; i < nums1.length; i++) {
        let flag = -1
        for (let j = nums2.indexOf(nums1[i]); j < nums2.length; j++) {
            if (nums2[j] > nums1[i]) {
                flag = nums2[j];
                break
            }
        }
        finalList.push(flag)
    }
    return finalList
};

console.log(nextGreaterElement([4, 1, 2], [1, 3, 4, 2]));
