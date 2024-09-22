const sorted_square = (arr) => {
    let newArr = [...arr]
    let j = 0
    let k = arr.length - 1
    for (let i = arr.length - 1; i > -1; i--) {
        const sqj = arr[j] * arr[j]
        const sqk = arr[k] * arr[k]
        console.log(j, "   ", k);
        console.log(newArr, "  ", sqk, "   ", i, "   ", sqj, "   ", arr);
        if (sqk > sqj) {
            newArr[i] = sqk
            k = k - 1
        } else {
            newArr[i] = sqj
            j = j + 1
        }
        console.log(j, "   ", k);
    }
    console.log(newArr);
    return newArr
}

sorted_square([-1, 0, 3, 5])