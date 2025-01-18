# @algorithm @lc id=1029 lang=python3 
# @title vertical-order-traversal-of-a-binary-tree


from en.Python3.mod.preImport import *
# @test([3,9,20,null,null,15,7])=[[9],[3,15],[20],[7]]
# @test([1,2,3,4,5,6,7])=[[4],[2],[1,5,6],[3],[7]]
# @test([1,2,3,4,6,5,7])=[[4],[2],[1,5,6],[3],[7]]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
        BFS/DFS + Hash Table
    """
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = defaultdict(list)

        def bfs():
            q = deque([(root, 0, 0)])
            while q:
                node, x, y = q.popleft()
                if node:
                    ans[y].append((x, node.val))
                    q.append((node.left, x+1, y-1))
                    q.append((node.right, x+1, y+1))

        def dfs(node, x, y):
            if node:
                ans[y].append((x, node.val))
                dfs(node.left, x+1, y-1)
                dfs(node.right, x+1, y+1)

        # bfs()
        dfs(root, 0, 0)
        return [[val for _, val in sorted(ans[x])] for x in sorted(ans)]