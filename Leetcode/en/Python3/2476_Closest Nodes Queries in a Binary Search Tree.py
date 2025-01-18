# @algorithm @lc id=2567 lang=python3 
# @title closest-nodes-queries-in-a-binary-search-tree


from en.Python3.mod.preImport import *
# @test([6,2,13,1,4,9,15,null,null,null,null,null,null,14],[2,5,16])=[[2,2],[4,6],[15,-1]]
# @test([4,null,9],[3])=[[-1,4]]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        nodes = []
        def inorder(node):
            if not node:
                return []
            inorder(node.left)
            nodes.append(node.val)
            inorder(node.right)
        inorder(root)

        ans = []
        for q in queries:
            idx1 = bisect_left(nodes, q) # Find the first element that is not less than q (>=)
            idx2 = bisect_right(nodes, q) # Find the first element that is greater than q (>)
            if idx1 != idx2: # q is in the tree
                ans.append([q, q])
            else:
                if idx1 == 0:
                    ans.append([-1, nodes[idx1]])
                elif idx1 == len(nodes):
                    ans.append([nodes[idx1-1], -1])
                else:
                    ans.append([nodes[idx1-1], nodes[idx1]])
        return ans