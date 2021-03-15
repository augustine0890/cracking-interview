# Problem: https://www.hackerrank.com/challenges/fraudulent-activity-notifications/
import bisect as bs

def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bs.bisect_left(a, x)
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
        bs.insort(heap, expenditure[ind])
        to_del += 1
            
    return times


if __name__ == "__main__":
    results = activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5)
    print(results)