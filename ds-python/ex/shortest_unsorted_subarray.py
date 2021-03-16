# Problem: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
# Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order,
# then the whole array will be sorted in ascending order.
# Approach 1:
from typing import List

def findUnsortedSubarray(self, nums: List[int]) -> int:
    nums_sorted = sorted(nums)
    first, last = 0, 0
    for i in range(len(nums)):
        if nums[i] != nums_sorted[i]:
            first = i
            break
    for j in range(len(nums),-1,-1):
        if nums[j] != nums_sorted[j]:
            last = j
            break
    if last-first == 0:
        return 0
    return (last-first) + 1

# Approach 2:

def findUnsortedSubarray(self, nums: List[int]) -> int:
    nums_sorted = sorted(nums)
    arr = []
    for i in range(len(nums)):
        if nums[i] != nums_sorted[i]:
            arr.append(i)
    if not len(arr):
        return 0
    if len(arr) == 1:
        return 1
    return (arr[-1] - arr[0]) + 1


array = [23, 32, 24, 52, 64]
for i in range(len(array)):
    print(array[i])