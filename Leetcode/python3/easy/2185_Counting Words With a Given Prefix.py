#
# @lc app=leetcode id=2185 lang=python3
# @lcpr version=30204
#
# [2185] Counting Words With a Given Prefix
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class TrieNode:
    def __init__(self):
        self.child = {}
        self.cnt = 0

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(w.startswith(pref) for w in words)
        root = TrieNode()
        node = root
        for ch in pref:
            if ch not in node.child:
                node.child[ch] = TrieNode()
            node = node.child[ch]

        for word in words:
            node = root
            for ch in word:
                if ch not in node.child:
                    break
                node = node.child[ch]
                node.cnt += 1
        
        node = root
        for ch in pref:
            node = node.child[ch]
        return node.cnt
# @lc code=end



#
# @lcpr case=start
# ["pay","attention","practice","attend"]\n"at"\n
# @lcpr case=end

# @lcpr case=start
# ["leetcode","win","loops","success"]\n"code"\n
# @lcpr case=end

#

