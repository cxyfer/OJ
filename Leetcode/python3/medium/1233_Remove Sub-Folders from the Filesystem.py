#
# @lc app=leetcode id=1233 lang=python3
# @lcpr version=30204
#
# [1233] Remove Sub-Folders from the Filesystem
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class TrieNode:
    def __init__(self):
        self.child = {}
        self.fid = -1

    def insert(self, path: str, i: int):
        node = self
        for p in path[1:].split("/"):
            if p not in node.child:
                node.child[p] = TrieNode()
            node = node.child[p]
        node.fid = i

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = TrieNode()
        for i, path in enumerate(folder):
            root.insert(path, i)
        
        ans = []
        def dfs(node: TrieNode):
            if node.fid != -1:
                ans.append(folder[node.fid])
                return
            for child in node.child.values():
                dfs(child)
        dfs(root)
        return ans
# @lc code=end



#
# @lcpr case=start
# ["/a","/a/b","/c/d","/c/d/e","/c/f"]\n
# @lcpr case=end

# @lcpr case=start
# ["/a","/a/b/c","/a/b/d"]\n
# @lcpr case=end

# @lcpr case=start
# ["/a/b/c","/a/b/ca","/a/b/d"]\n
# @lcpr case=end

#

