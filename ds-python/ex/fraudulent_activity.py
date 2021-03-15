# Problem: https://www.hackerrank.com/challenges/fraudulent-activity-notifications/
import bisect

def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

def median(a_sorted, days):
    half = len(a_sorted)//2
    
    if days % 2:
        median = a_sorted[half]
    median = (a_sorted[half-1] + a_sorted[half])/2
        
    return float(median)

def activityNotifications(expenditure, days):
    """
    expenditure -- an array of integers representing daily expenditures
    days -- an integer, the lookback days for median spending
    """
    heap = sorted(expenditure[:days])
    times = 0
    med = 0
    to_del = 0
    
    for ind in range(days, len(expenditure)):
        med = median(heap, days)
        #print("heap: {}".format(heap))
        #print("log[{}] = {} med = {}".format(ind, log[ind], med))
            
        if float(expenditure[ind]) >= 2*med:
            times += 1
        
        #del heap[heap.index(log[to_del])]
        del heap[index(heap, expenditure[to_del])]
        bisect.insort(heap, expenditure[ind])
        to_del += 1
            
    return times

# 2nd approach
from collections import deque
import statistics
"""
def median(arr):
    n = len(arr)
    mid = n//2

    if n % 2:
        return sorted(arr)[mid]
    return sum(sorted(arr)[mid-1:mid+1])/2

def activityNotifications(expenditure, days):
    times = 0
    a = expenditure[:days]
    a = deque(a)
    print(a)
    m = statistics.median(a)
    for i in range(days, len(expenditure)-1):
        if expenditure[i] >= 2*m:
            times += 1
        a.popleft()
        a.append(expenditure[i])
        print(a)
        m = statistics.median(a)
    return times
"""
def med(arr, d, m):
    if d % 2 == 0:
        return sum(arr[m - 1:m + 1]) / 2
    return arr[int(m)]

def activityNotifications(expenditure, d):
    n = len(expenditure)
    arr = sorted(expenditure[:d])
    m = d//2
    times = 0
        
    for i in range(d, n):
        if expenditure[i] >= 2*med(arr, d, m):        
            times += 1

        print(expenditure[i-d])
        del arr[bisect.bisect_left(arr, expenditure[i-d])]
        bisect.insort(arr, expenditure[i])
    
    return times

if __name__ == "__main__":
    results = activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5)
    print(results)