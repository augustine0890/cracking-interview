/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

const twoSum = function(nums, target) {
    let hash = {};
    for (let i = 0; i < nums.length; i++) {
        const j = target - nums[i];
        if (typeof hash[j] !== 'undefined') {
            return [hash[j], i];
        }
        hash[nums[i]] = i;
    }
    return [];
};

console.log(twoSum([2,7,11,15], 9));
console.log(twoSum([3,2,4], 6));