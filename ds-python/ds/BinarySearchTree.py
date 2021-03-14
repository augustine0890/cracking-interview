"""
A tree whose elements have at most two children is called a binary tree.
Each element in a binary tree can have only two children. A node's left child must
have a value less than its parent's value, and the node's right child must have a value
greater than its parent value.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data == self.data:
            return
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def in_order_traversal(self):
        elements = []

        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()
        # visit base node
        elements.append(self.data)

        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def pre_order_traversal(self):
        elements = []
        # base node
        elements.append(self.data)
        
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        
        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements

    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval) + " is not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval) + " is not Found"
            return self.right.findval(lkpval)
        else:
            return str(self.data) + " is found"

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            
            # min_val = self.right.find_min()
            # self.data = min_val
            # self.right = self.right.delete(min_val)
            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)
        
        return self

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()


def build_tree(elements):
    root = Node(elements[0])

    for i in range(1, len(elements)):
        root.insert(elements[i])
    
    return root
    
if __name__ == "__main__":
    numbers = [22, 12, 34, 32, 11, 9, 18, 45]
    numbers_tree = build_tree(numbers)
    print("In order traversal: ", numbers_tree.in_order_traversal())
    print("Pre order traversal: ", numbers_tree.pre_order_traversal())
    print("Post order traversal: ", numbers_tree.post_order_traversal())
    print(numbers_tree.findval(32))
    print(numbers_tree.findval(8))

    print("Min:",numbers_tree.find_min())
    print("Max:",numbers_tree.find_max())
    print("Sum:", numbers_tree.calculate_sum())

    numbers_tree.delete(32)
    print("In order traversal: ", numbers_tree.in_order_traversal())
