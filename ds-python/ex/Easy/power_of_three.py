# Problem: https://leetcode.com/problems/power-of-three/
# Time: O(logn)
# Space: O(1)
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            if n%3 != 0:
                return False
            n /= 3
        return True

# Problem: https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 1:
            n, r = divmod(n, 3)
            if r == 2:
                return False
        return True
