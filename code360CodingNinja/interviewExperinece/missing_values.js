const missingValues = (arr) => {
    const temp = {}; // Hashtable to track numbers
    const res = [];  // Array to store missing values

    // Populate the hashtable with the given array
    for (let i = 0; i < arr.length; i++) {
        temp[arr[i]] = true; // Mark the number as present
    }
    console.log(temp);

    // Find the missing numbers in the range
    const start = Math.min(...arr); // Smallest number in the array
    const end = Math.max(...arr);   // Largest number in the array

    for (let i = start; i <= end; i++) {
        if (!temp[i]) { // If the number is not in the hashtable
            res.push(i);
        }
    }

    return res;
}
console.log(missingValues([1, 3, 4, 6, 7, 8, 10]));