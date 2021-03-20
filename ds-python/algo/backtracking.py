"""
Example Algorithms of Backtracking
    - Binary Strings: generating all binary strings
    - Generating k-ary Strings
    - The Knapsack Problem
    - Hamiltonian Cycles
    - Graph Coloring Problem
"""
# Problem: Generate all the binary strings with n bits. Assume A[0..n-1] is an array of size n
# O(2^n) --> 2^n possibilites for n-bit string
def appendAtLeft(x, L):
    return [x + ele for ele in L]

def bitStrings(n):
    if n == 0: return []
    if n == 1: return ["0", "1"]
    else:
        return (appendAtLeft("0", bitStrings(n-1)) + appendAtLeft("1", bitStrings(n-1)))

# Problem: Generate all the strings of length n drawn from 0..k - 1
# Time: O(k^n) 
def rangeToList(k):
    result = []
    for i in range(0,k):
        result.append(str(i))
    return result

def baseKString(n, k):
    if n == 0: return []
    if n == 1: return rangeToList(k)
    return [digit+bitstring for digit in baseKString(1,k) for bitstring in baseKString(n-1,k)]

if __name__ == "__main__":
    print(bitStrings(3))
    print(baseKString(4,3))