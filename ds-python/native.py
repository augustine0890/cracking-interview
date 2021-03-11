z = ('Augustine', 'Kevin', 'David', 'Craig')
print(sorted(z))
print(sorted(z, key=lambda k: k[3]))

# Unpacking
x = ['pig', 'cow', 'horse']
a, b, c = x
print(a, b, c)

# List comprehension
a = [i**2 for i in range(10) if i>4]
print(a)

# Insert an item 
x = [5, 7, 9, 3]
x.insert(1, ['p', 'm'])
print(x)
x.reverse()
print(x)

# sorted(x) --> returns new sorted list
# x.sort() --> puts the items of x in sorted order (in place)

x = (1, 2, 3)
# del(x[1]) # fails
y = ([1, 2], 3)
del(y[0][1])
print(y)
y += (4,)
print(y)

"""
Sets
- Store non-duplicate items
- Very fast access vs Lists
"""

my_list = [20, 10, 25, 35]
total = sum(my_list)
lowest = min(my_list)
count = len(my_list)

odds = [x for x in range(10) if x%2 == 1]
print(odds)