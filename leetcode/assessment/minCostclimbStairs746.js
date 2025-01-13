/**
 * @param {number[]} cost
 * @return {number}
 */
//If we want to know the min cost to reach stair #n, It will be tremendously helpful to know the min cost to reach step #n-1 and step #n-2 (because we can reach step #n in one step from them)
// This is DP problen

let minCostClimbingStairs = function(cost) {
    for (let i = 2; i < cost.length; i++) {
        cost[i] = cost[i] + Math.min(cost[i-2], cost[i-1]);
    }
    return Math.min(cost[cost.length - 2], cost[cost.length - 1]);
};

console.log(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]));