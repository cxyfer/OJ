#
# @lc app=leetcode id=1858 lang=python3
# @lcpr version=30204
#
# [1858] Longest Word With All Prefixes
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
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                idx = ord(ch) - ord('a')
                if node.child[idx] is None:
                    node.child[idx] = TrieNode()
                node = node.child[idx]
            node.is_end = True
        ans = ""
        for word in words:
            node = root
            for ch in word:
                idx = ord(ch) - ord('a')
                node = node.child[idx]
                if not node.is_end:
                    break
            else:
                if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                    ans = word
        return ans
# @lc code=end



#
# @lcpr case=start
# ["k","ki","kir","kira", "kiran"]\n
# @lcpr case=end

# @lcpr case=start
# ["a", "banana", "app", "appl", "ap", "apply", "apple"]\n
# @lcpr case=end

# @lcpr case=start
# ["abc", "bc", "ab", "qwe"]\n
# @lcpr case=end

#

