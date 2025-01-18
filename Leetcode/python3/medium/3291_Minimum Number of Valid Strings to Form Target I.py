#
# @lc app=leetcode id=3291 lang=python3
# @lcpr version=30204
#
# [3291] Minimum Number of Valid Strings to Form Target I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.is_end = False

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                idx = ord(ch) - ord('a')
                if node.child[idx] is None:
                    node.child[idx] = TrieNode()
                node = node.child[idx]
            node.is_end = True
        
        @cache
        def dfs(i: int) -> int:
            if i == len(target):
                return 0
            res = float('inf')
            node = root
            for j in range(i, len(target)):
                idx = ord(target[j]) - ord('a')
                if node.child[idx] is None:
                    break
                res = min(res, dfs(j + 1) + 1)
                node = node.child[idx]
            return res
        
        return dfs(0) if dfs(0) != float('inf') else -1
# @lc code=end

sol = Solution()
print(sol.minValidStrings(["abc","aaaaa","bcdef"], "aabcdabc")) # 3
print(sol.minValidStrings(["abababab","ab"], "ababaababa")) # 2
print(sol.minValidStrings(["abcdef"], "xyz")) # -1
#
# @lcpr case=start
# ["abc","aaaaa","bcdef"]\n"aabcdabc"\n
# @lcpr case=end

# @lcpr case=start
# ["abababab","ab"]\n"ababaababa"\n
# @lcpr case=end

# @lcpr case=start
# ["abcdef"]\n"xyz"\n
# @lcpr case=end

#

