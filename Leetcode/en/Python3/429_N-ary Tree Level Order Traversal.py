# @algorithm @lc id=764 lang=python3 
# @title n-ary-tree-level-order-traversal


from en.Python3.mod.preImport import *
# @test([1,null,3,2,4,null,5,6])=[[1],[3,2,4],[5,6]]
# @test([1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14])=[[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = deque([root])
        while q:
            cur = []
            for _ in range(len(q)):
                node = q.popleft()
                cur.append(node.val)
                for child in node.children:
                    q.append(child)
            ans.append(cur)
        return ans