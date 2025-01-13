const binarySearch = (array, target) => {
    //write your code here
    let i = 0, j = array.length - 1, middle
    while (i <= j) {
        middle = Math.floor((i + j) / 2);
        console.log(i, j, middle, "   ", array[middle]);
        if (target === array[middle]) {
            return middle
        } else if (target < array[middle]) {
            j = middle - 1
        } else {
            i = middle + 1
        }
    }
    return -1
}

const binarySearchRecursive = function (nums, target) {
    const helper = function (nums, target, left, right) {
        //base case
        if (left > right) return -1;
        const middle = Math.floor((left + right) / 2);
        if (target === nums[middle]) return middle;
        else if (target < nums[middle]) return helper(nums, target, left, middle - 1);
        else return helper(nums, target, middle + 1, right);
    }
    return helper(nums, target, 0, nums.length - 1);
}

console.log(binarySearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3))