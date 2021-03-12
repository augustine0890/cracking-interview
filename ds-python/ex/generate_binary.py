"""
Generate Binary Numbers from 1 to n
- The next two numbers are formed by adding a '0' and '1' to the previous number.
- Create the empty queue of strings
- Enqueue the first binary number '1' to queue
- Loop n binary numbers:
    - Dequeue and print the front of queue
    - Generate the next two binary number by adding a '0' and '1'
    - Enqueue those two bin number into the queue
"""
from collections import deque

def generateBinary(n):
    q = deque()

    # Enqueue the first binary number
    q.append("1")

    while (n>0):
        n -= 1
        s1 = q.popleft()
        print(s1)
        
        s2 = s1
        q.append(s1+"0")
        q.append(s2+"1")

n = 10
generateBinary(n)
