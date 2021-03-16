# Problem: https://leetcode.com/problems/best-sightseeing-pair/
# max: A[i] + A[j] + i - j
from typing import List

# Approach 1:
# O(max(values) * N)
# N: length of values array
# max value for array is 1000, whereas max length for array is 50000
def maxScoreSightseeingPair(self, values: List[int]) -> int:
    curr = best = 0
    for i in range(len(values)):
        val = values[i] + i
        j = i + 1
        while j < len(values) and j < val + 1:
            curr = val - j + values[j]
            best = max(curr, best)
    
    return best

# Approach 2
# Time: O(n)
def maxScoreSightseeingPair(self, values: List[int]) -> int:
    prev = best = 0
    for i in range(len(values)):
        best = max(best, values[i] - i + prev) # A[j] - j + prev: A[i] + i
        prev = max(prev, values[i] + i) # A[i] + i
    return best


def maxScoreSightseeingPair(self, A):
    """
    :type A: List[int]
    :rtype: int
    """
    result, curr = 0, 0
    for x in A:
        result = max(result, curr+x)
        curr = max(curr, x)-1
    return result
