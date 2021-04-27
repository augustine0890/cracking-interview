/**
 * @param {number} n
 * @returns {number}
 */

const climbStairs = function(n) {
    // base case
    if (n <= 1) return 1;
    // fib sequence f(n) = f(n-1) + f(n-2)
    return climbStairs(n-1) + climbStairs(n-2);
};

// Iterative solution with memoization
const climbStairs2 = function(n) {
    let steps = [1, 1];
    for (let i = 2; i < n + 1; i++) {
        steps.push(steps[n - 1] + steps[n - 2]);
    }
    return steps[n];
};