"""
FIFO: First-In First-Out
Enqueue: add an item to the end of the line
Dequeue: remove an item from the front of the line
"""

from collections import deque
my_queue = deque()
my_queue.append(2)
my_queue.append(7)
print(my_queue)
print(my_queue.popleft())

class Queue:
    def __init__(self):
        self.queue = deque()
        self.size = 0
    def enqueue(self, item):
        self.queue.append(item)
        self.size += 1
    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.queue.popleft()
        else: 
            return None
    def peek(self):
        if self.size > 0:
            ret_val = self.queue.popleft()
            self.queue.appendleft(ret_val)
            return ret_val
        else:
            return None
    def get_size(self):
        return self.size