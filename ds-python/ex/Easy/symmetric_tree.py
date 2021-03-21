# Time: O(n)
# Space: O(h)
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)
    
    def isMirror(self, root1: TreeNode, root2: TreeNode) -> bool:
        if (not root1) and (not root2): return True
        if (not root1) or (not root2): return False
        return (root1.val == root2.val) and self.isMirror(root1.left, root2.right) and \
            self.isMirror(root1.righ, root2.left)


