# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def check(p,q):
            if not p and not q:
                return True
            elif p and q:
                #print(p.val, " and " , q.val)
                #print(p.val == q.val and check(p.left, q.left) and check(p.right, q.right))
                return p.val == q.val and check(p.left, q.left) and check(p.right, q.right)
            else:
                #print("false .....")
                return False 

        return check(p,q)

            