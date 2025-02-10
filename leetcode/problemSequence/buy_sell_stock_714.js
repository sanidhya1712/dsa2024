/**
 * @param {number[]} prices
 * @param {number} fee
 * @return {number}
 */
var maxProfit = function (prices, fee) {
    let free = [];      // signifies do nothing or sell
    let hold = [];      // signifies buy
    hold[0] = -prices[0]
    free[0] = 0
    for (let i = 1; i < prices.length; i++) {
        hold[i] = Math.max(hold[i - 1], free[i - 1] - prices[i])
        free[i] = Math.max(free[i - 1], hold[i - 1] + prices[i] - fee)
    }

    return free[free.length - 1]
};

console.log(maxProfit([1, 3, 2, 8, 4, 9], 2));
