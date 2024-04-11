class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isBetween(root, left, right):
            # base case
            if root is None:
                return True

            # if root val meets parameters then check left and right
            # update parameters when checking left and right
            if root.val > left and root.val < right:
                # check left and right (if going right update left and vice versa)
                return isBetween(root.left, left, root.val) and isBetween(root.right, root.val, right)

            # if root val doesn't meet parameters then it must be invalid
            else:
                return False

        return isBetween(root, float(-inf), float(inf))



# cool not my solution
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         l = []
#         def traverse(root):
#             if(root.left):
#                 traverse(root.left)
#             l.append(root.val)
#             if(root.right):
#                 traverse(root.right)
#         traverse(root)
#         for i in range(1,len(l)):
#             if(l[i-1] >= l[i]):
#                 return False
#         return True