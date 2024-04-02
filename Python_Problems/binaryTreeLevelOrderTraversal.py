# Probably not an ideal solution. If I were to do it again I would probably use DFS
# and potentially an array and indexes based on the level I was currently on

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def helper_lo(answer, cur_nodes):
            add_to_answer = []
            new_nodes = []
            for node in cur_nodes:
                if node:
                    add_to_answer.append(node.val)
                    if node.left:
                        new_nodes.append(node.left)
                    if node.right:
                        new_nodes.append(node.right)

            answer.append(add_to_answer)

            if not new_nodes:
                return answer
            else:
                return helper_lo(answer, new_nodes)

        if root:
            return helper_lo([], [root])
        else:
            return []