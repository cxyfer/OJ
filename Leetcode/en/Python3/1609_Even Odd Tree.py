# @algorithm @lc id=1731 lang=python3 
# @title even-odd-tree


from en.Python3.mod.preImport import *
# @test([1,10,4,3,null,7,9,12,8,6,null,null,2])=true
# @test([5,4,2,3,3,7])=false
# @test([5,9,1,3,5,7])=false
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        # return self.solve1(root)
        # return self.solve2(root)
        return self.solve3(root)
    def solve1(self, root: Optional[TreeNode]) -> bool:
        def isIncreasing(arr: List[int]) -> bool:
            for i in range(1, len(arr)):
                if arr[i] <= arr[i - 1]: return False
            return True
        q = deque([root])
        level = 0
        while q:
            arr = []
            for _ in range(len(q)):
                node = q.popleft()
                arr.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            if level % 2 == 0: # even
                if any(x % 2 == 0 for x in arr): return False
                if not isIncreasing(arr): return False
            else: # odd
                if any(x % 2 == 1 for x in arr): return False
                if not isIncreasing(arr[::-1]): return False
            level += 1
        return True
    def solve2(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        level = 0
        while q:
            prev = float('inf') if level % 2 else float('-inf')
            for _ in range(len(q)):
                node = q.popleft()
                if node.val % 2 == level % 2 or (level % 2 == 0 and node.val <= prev) or (level % 2 == 1 and node.val >= prev):
                    return False
                prev = node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            level += 1
        return True
    def solve3(self, root: Optional[TreeNode]) -> bool:
        last = dict() # 紀錄每一層的最後一個數字
        
        def dfs(node, level):
            prev = last.get(level, float('inf') if level % 2 else float('-inf') ) 
            if node.val % 2 == level % 2 or (level % 2 == 0 and node.val <= prev) or (level % 2 == 1 and node.val >= prev):
                return False
            last[level] = node.val
            if node.left and not dfs(node.left, level + 1):
                return False
            if node.right and not dfs(node.right, level + 1):
                return False
            return True
        
        return dfs(root, 0)