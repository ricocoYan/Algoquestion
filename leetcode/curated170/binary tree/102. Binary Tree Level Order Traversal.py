# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

# 目的是把当前层级的level都计算完
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # None root
        if not root:
            return []


        queue = collections.deque()
        queue.append(root)

        currentlevel = 0
        result = []

        while queue:
            result.append([])
            length = len(queue)

            for i in range(length):
                ele = queue.popleft()
                result[currentlevel].append(ele.val)
                if ele.left:
                    queue.append(ele.left)
                if ele.right:
                    queue.append(ele.right)

            currentlevel += 1

        return result

