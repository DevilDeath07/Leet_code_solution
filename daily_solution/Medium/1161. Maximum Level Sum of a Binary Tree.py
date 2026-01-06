# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # BFS to split levels and find max sum
        queue = deque([root])
        max_sum = float('-inf')
        max_level = 1
        level = 1

        while queue:
            level_size = len(queue)
            level_sum = 0
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if level_sum > max_sum: 
                max_sum = level_sum 
                max_level = level 
            level += 1
        return max_level
