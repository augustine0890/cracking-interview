# Problem: https://www.hackerrank.com/challenges/largest-rectangle/problem
import sys

def largestRectangle(h):
    area = 0

    for i in range(len(h)):
        length = 0
        for j in range(i, -1, -1):
            if h[j] >= h[i]:
                length += 1
            else:
                break
        
        for j in range(i+1, len(h)):
            if h[j] >= h[i]:
                length += 1
            else:
                break
        
        area = max(area, h[i]*length)
    
    return area


h = [1, 2, 3, 4, 5]
result = largestRectangle(h)
print(result)

# if __name__ == "__main__":
    # n = int(input().strip())
    # h = list(map(int, input().strip().split(' ')))
    # result = largestRectangle(h)
    # print(result)
