#
# @lc app=leetcode id=2196 lang=python3
# @lcpr version=30204
#
# [2196] Create Binary Tree From Descriptions
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        mp = dict()  # val -> TreeNode
        fa = dict()  # fa[child] = parent
        for pa, ch, is_left in descriptions:
            if pa not in mp:
                mp[pa] = TreeNode(val=pa)
            if ch not in mp:
                mp[ch] = TreeNode(val=ch)
            if is_left:
                mp[pa].left = mp[ch]
            else:
                mp[pa].right = mp[ch]
            fa[ch] = pa

        rt = descriptions[0][0]
        while rt in fa:
            rt = fa[rt]
        return mp[rt]


class Solution2:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        n = len(descriptions) + 1

        nodes = set()
        for pa, ch, is_left in descriptions:
            nodes.add(pa)
            nodes.add(ch)
        nodes = list(nodes)
        val_to_idx = {u: i for i, u in enumerate(nodes)}

        fa = list(range(n))

        def find(x: int) -> int:
            while fa[x] != x:
                fa[x] = fa[fa[x]]
                x = fa[x]
            return x

        def union(x: int, y: int) -> bool:
            fx, fy = find(x), find(y)
            if fx == fy:
                return False
            fa[fy] = fx
            return True

        mp = dict()  # val -> TreeNode
        for pa, ch, is_left in descriptions:  # u -> v
            if pa not in mp:
                mp[pa] = TreeNode(val=pa)
            if ch not in mp:
                mp[ch] = TreeNode(val=ch)
            if is_left:
                mp[pa].left = mp[ch]
            else:
                mp[pa].right = mp[ch]
            union(val_to_idx[pa], val_to_idx[ch])
        rt = find(val_to_idx[descriptions[0][0]])
        return mp[nodes[rt]]


Solution = Solution1
# Solution = Solution2
# @lc code=end



#
# @lcpr case=start
# [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,1],[2,3,0],[3,4,1]]\n
# @lcpr case=end

#

