from node import Node

class LinkedList:
  def __init__(self):
    self.head_node = None
  
  def get_head(self):
    return self.head_node
  
  def is_empty(self):
    if self.head_node is None:
      return True
    else:
      return False
  
  def insert_at_head(self, dt):
    temp_node = Node(dt)
    if self.is_empty():
      self.head_node = temp_node
      return self.head_node
    temp_node.next_element = self.head_node
    self.head_node = temp_node
    return self.head_node
  
  # Insert a value at the end of the list
  def insert_at_tail(self, dt):
    new_node = Node(dt)
    if self.get_head() is None:
      self.head_node = new_node
      return
    temp = self.get_head()
    while temp.next_element is not None:
      temp = temp.next_element
    temp.next_element = new_node
    return
  
  def length(self):
    curr = self.get_head()
    length = 0

    while curr is not None:
      length += 1
      curr = curr.next_element
    return length
  
  def print_list(self):
    if self.is_empty():
      print("List is Empty")
      return False
    temp = self.head_node
    while temp.next_element is not None:
      print(temp.data, end=" -> ")
      temp = temp.next_element
    print(temp.data, "--> None")
    return True

  def delete_at_head(self):
    first_element = self.get_head()
    if first_element is not None:
      self.head_node = first_element.next_element
      first_element.next_element = None
    return
  
  def delete(self, value):
    deleted = false
    if self.is_empty():
      print("List is Empty")
      return deleted
    curr = self.get_head()
    prev = None
    if curr.data is value:
      self.delete_at_head()
      deleted = True
      return deleted
    
    # Traversing for Node to Delete
    while curr is not None:
      if value is curr.data:
        prev.next_element = curr.next_element
        curr.next_element = None
        deleted = True
        break
      prev = curr
      curr = curr.next_element
    return deleted
  
  def search(self, dt):
    if self.is_empty():
      print("List is Empty")
      return None
    temp = self.head_node
    while temp is not None:
      if temp.data is dt:
        return temp
      temp = temp.next_element
    print(dt, " is not in List")
    return None
  
  def remove_duplicates(self):
    if self.is_empty():
      return
    
    # If list only has one node, leave it unchanged
    if self.get_head().next_element is None:
      return
    
    outer_node = self.get_head()
    while outer_node:
      inner_node = outer_node
      while inner_node:
        if inner_node.next_element:
          if outer_node.data == inner_node.next_element.data:
            # Duplicates found
            new_next_element = inner_node.next_element.next_element
            inner_node.next_element = new_next_element
          else:
            # Otherwise simply iterate ahead
            inner_node = inner_node.next_element
        else:
          inner_node = inner_node.next_element
      outer_node = outer_node.next_element
    return
