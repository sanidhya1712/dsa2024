const process = require('process');
console.log('Start');
const fs = require('fs');
fs.readFile('test.txt', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log(data);
});
console.log('File read initiated');
setTimeout(() => {
    console.log('Timeout');
}, 0);
setImmediate(() => {
    console.log('Immediate');
});
Promise.resolve().then(() => {
    console.log('Promise');
});
process.nextTick(() => {
    console.log('Next Tick');
})


function outer() {
    let a = 1;
    function inner() {
        a++
        console.log(a);
        var a = 2;
        console.log(a);
    }
    inner();
}
outer();

console.log('End');
let s = "abcde";
s = s.split("");
let b = s.reverse();
console.log(b);