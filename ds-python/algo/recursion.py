"""
- Generally, iterative solutions are more efficient than recursive solutions (due to the overhead of function calls)
"""
# calcualte factorial
def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)


# Prblems: Given an array, check whether the array is in sorted order
# Time: O(n)
# Space: O(n) for recursive stack space
def isArrayInSortedOrder(A):
    # base case
    if len(A) == 1:
        return True
    return A[0] <= A[1] and isArrayInSortedOrder(A[1:])


if __name__ == "__main__":
    print(factorial(3))
    print(factorial(6))
    print(factorial(7))

    A = [134, 536, 634, 633, 642, 798, 983]
    B = [134, 536, 634, 776, 842, 898, 983]
    print(isArrayInSortedOrder(A))
    print(isArrayInSortedOrder(B))
    
