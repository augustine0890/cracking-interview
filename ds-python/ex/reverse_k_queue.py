"""
Reversing the first K elements of a Queue
- Create an empty stack
- Dequeue first K items from queue and push the dequeued items to stack
- Pop items from stack to the the queue
- Time complexity: O(n+k)
"""
from collections import deque

def rerverseKElements(k, queue):
    if (not queue) or (k > len(queue)):
        return
    if k <= 0:
        return

    stack = []
    n = k
    while (k>1):
        k -= 1
        stack.append(queue.popleft())
        
    while (n>1):
        n -= 1
        queue.append(stack.pop())
    
    print(queue)

q = deque()
Q = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for e in Q:
    q.append(e)

rerverseKElements(k=5, queue=q)
