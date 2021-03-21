from collections import deque

# Time: O(n)
# Space: O(n/2) -> O(h)
class Solution:
    def levelOrder(self, root: TreeNode) -> List(List[int]):
        result = []
        if not root:
            return result
        
        queue = deque()
        queue.append(root)
        while queue:
            qLen = len(queue)
            currentLevel = []
            for i in range(qLen):
                node = queue.popleft()
                if node:
                    currentLevel.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if currentLevel:
                result.append(currentLevel)
        
        return result