#
# @lc app=leetcode id=2416 lang=python3
# @lcpr version=30204
#
# [2416] Sum of Prefix Scores of Strings
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.cnt = 0

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        n = len(words)

        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                idx = ord(ch) - ord('a')
                if node.child[idx] is None:
                    node.child[idx] = TrieNode()
                node = node.child[idx]
                node.cnt += 1

        ans = [0] * n
        for i, word in enumerate(words):
            node = root
            score = 0
            for ch in word:
                idx = ord(ch) - ord('a')
                node = node.child[idx]
                score += node.cnt
            ans[i] = score
        return ans
# @lc code=end



#
# @lcpr case=start
# ["abc","ab","bc","b"]\n
# @lcpr case=end

# @lcpr case=start
# ["abcd"]\n
# @lcpr case=end

#

