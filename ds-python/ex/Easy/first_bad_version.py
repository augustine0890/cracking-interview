# Time: O(logn)
# Space: O(1)
first_bad = 0
def isBadVersion(version):
    if version >= first_bad:
        return True
    return False


class Solution:
    def firstBadVersion(self, n):
        i, j = 0, n
        while i <= j:
            mid = i + (j - i) // 2
            if isBadVersion(mid):
                j = mid - 1
            else:
                i = mid + 1
        
        if isBadVersion(mid):
            return mid
        return mid+1


if __name__ == "__main__":
    first_bad = 7
    s = Solution()
    print(s.firstBadVersion(10))