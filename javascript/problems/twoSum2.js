function twoSum(numbers, target) {
  let lo = 0;
  let hi = numbers.length - 1;
  let sum;
  while (lo < hi) {
    sum = numbers[lo] + numbers[hi];
    if (sum === target) {
      return [lo+1, hi+1]
    } else if (sum < target) {
      lo++;
    } else {
      hi--;
    }
  }
  return [];
}

console.log(twoSum([2,7,11,15], 9));
console.log(twoSum([2,3,4], 6));
console.log(twoSum([2,7,11,15], 2));
console.log(twoSum([-1,0], -1));