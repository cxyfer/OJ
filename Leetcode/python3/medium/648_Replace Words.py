#
# @lc app=leetcode id=648 lang=python3
# @lcpr version=30203
#
# [648] Replace Words
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    1. Hash Set
    2. Trie
"""
class Solution1:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        d = set(dictionary) # hash set
        ans = []
        for word in sentence.split(" "):
            for i in range(1, len(word)+1):
                if word[:i] in d:
                    ans.append(word[:i])
                    break
            else:
                ans.append(word)
        return " ".join(ans)
    
class SegmentTreeNode: # Trie
    def __init__(self):
        self.child = [None] * 26
        self.isEnd = False
    
class Solution2:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = SegmentTreeNode()
        for word in dictionary:
            cur = root
            for ch in word:
                idx = ord(ch) - ord("a")
                if cur.child[idx] is None:
                    cur.child[idx] = SegmentTreeNode()
                cur = cur.child[idx]
            cur.isEnd = True
        ans = []
        for word in sentence.split(" "):
            cur = root
            for i, ch in enumerate(word):
                idx = ord(ch) - ord("a")
                cur = cur.child[idx]
                if cur is None: # no prefix, case 1
                    ans.append(word)
                    break
                if cur.isEnd: # find prefix
                    ans.append(word[:i+1])
                    break
            else: # no prefix, case 2
                ans.append(word)
        return " ".join(ans)
    
class Solution(Solution2):
    pass
# @lc code=end

sol = Solution()
print(sol.replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery"))
print(sol.replaceWords(["a","b","c"], "aadsfasf absbs bbab cadsfafs"))

#
# @lcpr case=start
# ["cat","bat","rat"]\n"the cattle was rattled by the battery"\n
# @lcpr case=end

# @lcpr case=start
# ["a","b","c"]\n"aadsfasf absbs bbab cadsfafs"\n
# @lcpr case=end

#

