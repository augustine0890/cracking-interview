from typing import List
import sys
# Time: O(n)
# Space: O(1)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        i, j = 0, len(s)-1
        while j >= i:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        # # Swap
        # tmp = s[i]
        # s[i] = s[j]
        # s[j] = tmp
    
    def reverse(self, x: int) -> int:
        MIN = -(sys.maxsize) # -(2**31)
        MAX = sys.maxsize - 1 #2**31 - 1
        
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        
        y = 0
        while x:
            digit = x % 10
            x //= 10
            y = (y*10) + digit
        
        if y > MAX or y < MIN:
            return 0
        
        return y*sign


if __name__ == "__main__":
    s = Solution()
    print(s.reverse(321))
    print(s.reverse(-321))