/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}

var multiply = function(num1, num2) {
    num1 = Number(num1)
    num2 = Number(num2)
    return String(num1* num2)
};
*/
var multiply = function(num1, num2) {
    if(num1== '0' || num2=='0')return '0';
    let result = Array(num1.length+num2.length).fill(0)
    for(let i=num1.length-1; i>=0; i--){
        for(let j=num2.length-1; j >= 0;  j--){
            let digit = parseInt(num1[i])*parseInt(num2[j]);
            let p1 = i+j, p2 = i+j+1;
            let sum = digit + result[p2] + result[p1] * 10; 
            result[p1] = Math.floor(sum / 10);
            result[p2] = sum % 10;
        }
    }
    while(result[0] === 0 && result.length>1)
    result.shift();
    return result.join("");
};

console.log(multiply("123", "456"));
