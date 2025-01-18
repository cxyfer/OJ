# @algorithm @lc id=2461 lang=python3 
# @title amount-of-time-for-binary-tree-to-be-infected


from en.Python3.mod.preImport import *
# @test([1,5,3,null,4,10,6,9,2],3)=4
# @test([1],1)=0
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
        BFS
    """
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        g = defaultdict(list)
        def dfs(u: TreeNode, fa: TreeNode) -> None:
            if not u: return
            if fa: 
                g[u.val].append(fa.val)
                g[fa.val].append(u.val)
            dfs(u.left, u)
            dfs(u.right, u)
        dfs(root, None) # build graph
        q = deque([(start, 0)])
        vis = {start}
        ans = 0
        while q:
            u, t = q.popleft()
            ans = max(ans, t)
            for v in g[u]:
                if v not in vis:
                    vis.add(v)
                    q.append((v, t+1))
        return ans