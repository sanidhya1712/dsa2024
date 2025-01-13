// const k_rotate_array = (arr, k) => {
//     if (arr.length <= 1) {
//         return arr
//     }
//     k = Math.abs(k % arr.length)
//     for (let i = 0; i < k; i++) {
//         console.log(arr.slice(arr.length - 1, arr.length), "   ", arr.slice(0, arr.length - 1));
//         arr = arr.slice(arr.length - 1, arr.length) + arr.slice(0, arr.length - 1)
//     }
//     return arr
// }
// optimum solution
const reverse = function (nums, start, end) {
    while (start < end) {
        [nums[start], nums[end]] = [nums[end], nums[start]];
        start++;
        end--;
    }
}

const k_rotate_array = function (nums, k) {
    k = k % nums.length; //k=102 ,length =5, 2 rotations
    //nums.reverse();
    reverse(nums, 0, nums.length - 1);
    //start =0, end = k-1
    reverse(nums, 0, k - 1);
    //start = k, end = length-1
    reverse(nums, k, nums.length - 1);
    return nums;
}

console.log(k_rotate_array([-1, 0, 3, 5], 9));