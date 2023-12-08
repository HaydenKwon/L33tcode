# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#loop through level by level

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if(root == None):
            return []
        ans = []
        current_level = [root]
        next_level = []
        ans_level = []
        while(len(current_level) > 0):
            for i in current_level:
                ans_level.append(i.val)
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            current_level = next_level
            next_level = []
            ans.append(ans_level)
            ans_level = []
        return ans
