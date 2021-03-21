"""
- MinHeap: every node greater than it's parent
    - Insert: O(logn), remove min: O(logn)
		- Parent: index // 2
		- Left Child: index * 2
		- Right Child: (index * 2) + 1
- .heapify_up() to compare the new element with its parent, making swaps if it violates the heap property: children must be greater than their parents.
- .heapify_down() to compare the new root with its children, swapping with the smaller child if necessary.
- MaxHeap: complete Binary Tree. Every node less than it's parent
    - Insert: O(logn), get max: O(1), remove max: O(logn)
"""
class MinHeap:
  def __init__(self):
  	self.heap_list = [None]
  	self.count = 0

  # HEAP HELPER METHODS
  def parent_idx(self, idx):
    return idx // 2

  def left_child_idx(self, idx):
    return idx * 2

  def right_child_idx(self, idx):
    return idx * 2 + 1

  def child_present(self, idx):
    return self.left_child_idx(idx) <= self.count

  # END OF HEAP HELPER METHODS

  def retrieve_min(self):
    if self.count == 0:
      print("No items in heap")
      return None
    
    min = self.heap_list[1]
    print("Removing: {0} from {1}".format(min, self.heap_list))
    self.heap_list[1] = self.heap_list[self.count]
    self.count -= 1
    self.heap_list.pop()
    print("Last element moved to first: {0}".format(self.heap_list))    
    self.heapify_down()
    return min

  def add(self, element):
    self.count += 1
    print("Adding: {0} to {1}".format(element, self.heap_list))
    self.heap_list.append(element)
    self.heapify_up()


  def get_smaller_child_idx(self, idx):
    if self.right_child_idx(idx) > self.count:
      print("There is only a left child")
      return self.left_child_idx(idx)
    else:
      left_child = self.heap_list[self.left_child_idx(idx)]
      right_child = self.heap_list[self.right_child_idx(idx)]
      if left_child < right_child:
        print("Left child is smaller")
        return self.left_child_idx(idx)
      else:
        print("Right child is smaller")
        return self.right_child_idx(idx)
	
	# maintaining the heap properties as we add additional elements
  def heapify_up(self):
    idx = self.count
    while self.parent_idx(idx) > 0:
      if self.heap_list[self.parent_idx(idx)] > self.heap_list[idx]:
        tmp = self.heap_list[self.parent_idx(idx)]
        print("swapping {0} with {1}".format(tmp, self.heap_list[idx]))
        self.heap_list[self.parent_idx(idx)] = self.heap_list[idx]
        self.heap_list[idx] = tmp
      idx = self.parent_idx(idx)
    print("HEAP RESTORED! {0}".format(self.heap_list))
    print("")
      
  def heapify_down(self):
    idx = 1
    while self.child_present(idx):
      smaller_child_idx = self.get_smaller_child_idx(idx)
      if self.heap_list[idx] > self.heap_list[smaller_child_idx]:
        tmp = self.heap_list[smaller_child_idx]
        print("swapping {0} with {1}".format(self.heap_list[idx], tmp))
        self.heap_list[smaller_child_idx] = self.heap_list[idx]
        self.heap_list[idx] = tmp

      idx = smaller_child_idx
    print("HEAP RESTORED! {0}".format(self.heap_list))
    print("")    

if __name__ == "__main__":
	# an instance of MinHeap to use
	min_heap = MinHeap()

	# the internal list for our example
	min_heap.heap_list = [None, 10, 13, 21, 61, 22, 23, 99]
	print(min_heap.heap_list)

	# example of how to use the helper methods:
	print("the parent index of 4 is:")
	print(min_heap.parent_idx(4))
	print("the left child index of 3 is:")
	print(min_heap.left_child_idx(3))

	# now it's your turn!
	# replace 'None' below using the correct helper methods and indexes
	idx_2_left_child_idx = min_heap.left_child_idx(2)
	print("The left child index of index 2 is:")
	print(idx_2_left_child_idx)
	print("The left child element of index 2 is:")
	# uncomment the line below to see the result in your console!
	print(min_heap.heap_list[idx_2_left_child_idx])

	idx_3_parent_idx = min_heap.parent_idx(3)
	print("The parent index of index 3 is:")
	print(idx_3_parent_idx)
	print("The parent element of index 3 is:")
	# uncomment the line below to see the result in your console!
	print(min_heap.heap_list[idx_3_parent_idx])

	idx_3_right_child_idx = min_heap.right_child_idx(3)
	print("The right child index of index 3 is:")
	print(idx_3_right_child_idx)
	print("The right child element of index 3 is:")
	# uncomment the line below to see the result in your console!
	print(min_heap.heap_list[idx_3_right_child_idx])
