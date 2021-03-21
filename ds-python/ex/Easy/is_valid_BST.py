class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, float("-inf"), float("inf"))
    
    def helper(self, root, low, high):
        if not root:
            return True
        return low < root.val and root.val < high and \
            self.helper(root, low, root.val) and \
            self.helper(root, root.val, high)