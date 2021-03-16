# Problem: https://leetcode.com/problems/trapping-rain-water/
"""
If there is a larger wall to the right then the water can be retained with height equal to the smaller wall on the left.
If there are no larger walls to the right then start from the left.
- Loop from index 0 to then end
- If a wall greater than or equal to the previous wall is encountered the make note of the index of that wall
- Keep adding previous wall's height minus the current (ith) wall to the variable water.
- Have a temporary variable that stores the same value as water.
- If no wall greater than or equal to the previous wall is found then quit.
- If prev_index < size of the input array then subtract the temp variable from water, and loop from end of the input array to prev_index and find a wall greater than or equal to the previous wall (in this case, the last wall from backwards).
"""

from typing import List

def trap(self, height: List[int]) -> int:
    size = len(height) - 1
 
    # Let the first element be stored as
    # previous, we shall loop from index 1
    prev = height[0]
 
    # To store previous wall's index
    prev_index = 0
    water = 0
 
    # To store the water until a larger wall
    # is found, if there are no larger walls
    # then delete temp value from water
    temp = 0
    for i in range(1, size + 1):
 
        # If the current wall is taller than
        # the previous wall then make current
        # wall as the previous wall and its
        # index as previous wall's index
        # for the subsequent loops
        if (height[i] >= prev):
            prev = height[i]
            prev_index = i
 
            # Because larger or same height wall is found
            temp = 0
        else:
 
            # Since current wall is shorter than
            # the previous, we subtract previous
            # wall's height from the current wall's
            # height and add it to the water
            water += prev - height[i]
 
            # Store the same value in temp as well
            # If we dont find any larger wall then
            # we will subtract temp from water
            temp += prev - height[i]
 
    # If the last wall was larger than or equal
    # to the previous wall then prev_index would
    # be equal to size of the array (last element)
    # If we didn't find a wall greater than or equal
    # to the previous wall from the left then
    # prev_index must be less than the index
    # of the last element
    if (prev_index < size):
 
        # Temp would've stored the water collected
        # from previous largest wall till the end
        # of array if no larger wall was found then
        # it has excess water and remove that
        # from 'water' var
        water -= temp
 
        # We start from the end of the array, so previous
        # should be assigned to the last element
        prev = height[size]
 
        # Loop from the end of array up to the 'previous index'
        # which would contain the "largest wall from the left"
        for i in range(size, prev_index - 1, -1):
 
            # Right end wall will be definitely smaller
            # than the 'previous index' wall
            if (height[i] >= prev):
                prev = height[i]
            else:
                water += prev - height[i]
 
    # Return the maximum water
    return water
    
    
    
    
    
    
    
    
