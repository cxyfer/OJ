# @algorithm @lc id=2646 lang=python3 
# @title kth-largest-sum-in-a-binary-tree


from en.Python3.mod.preImport import *
# @test([5,8,9,2,1,3,7,4,6],2)=13
# @test([1,2,null,3],1)=3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        hp = [] # min heap, size k
        q = deque([root])
        while q:
            cur = 0
            for _ in range(len(q)):
                node = q.popleft()
                cur += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if len(hp) < k:
                heappush(hp, cur)
            else:
                if cur > hp[0]:
                    heapreplace(hp, cur) # first pop then push
        return hp[0] if len(hp) == k else -1