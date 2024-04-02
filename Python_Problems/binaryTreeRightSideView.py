from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        results = []
        queue_level = len(queue)

        while queue_level:
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            queue_level -= 1

            if not queue_level:
                results.append(node.val)
                queue_level = len(queue)

        return results


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        def dfs(node, level, result):
            if not node:
                return

            if level >= len(result):
                result.append(node.val)

            if node.right:
                dfs(node.right, level + 1, result)

            if node.left:
                dfs(node.left, level + 1, result)

        result = []
        dfs(root, 0, result)

        return result
