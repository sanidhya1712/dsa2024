function allPermutation(nums) {
    if (nums.length == 0) return [[]];
    const permutation = [];
    function helper(nums, i) {
        if (i === nums.length - 1) {
            console.log(i, "--push time--", nums);
            permutation.push(nums.slice());
            return;
        }
        for (let j = i; j < nums.length; j++) {
            //swap i,j
            [nums[i], nums[j]] = [nums[j], nums[i]];
            console.log(j, i, "before -- ", nums);
            //recursive
            helper(nums, i + 1);
            //swap i,j 
            console.log(j, i, "after -- ", nums);
            [nums[i], nums[j]] = [nums[j], nums[i]];
        }
    }
    helper(nums, 0);
    return permutation;
}

console.log(allPermutation([1, 2, 3]));