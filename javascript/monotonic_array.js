const monotonic_array = (arr) => {
    if (arr.length <= 1) {
        return true
    }
    if (arr[0] < arr[arr.length - 1]) {
        for (let i = 0; i < arr.length - 1; i++) {
            if (arr[i + 1] < arr[i]) {
                return false
            }
        }
        return true
    } else {
        for (let i = 0; i < arr.length - 1; i++) {
            if (arr[i + 1] > arr[i]) {
                return false
            }
        }
        return true
    }
}

console.log(monotonic_array([-1, 0, 3, 5]));