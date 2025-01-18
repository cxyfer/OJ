#
# @lc app=leetcode.cn id=1268 lang=python3
#
# [1268] 搜索推荐系统
#
from en.Python3.mod.preImport import *
# @lc code=start
class Trie:
    def __init__(self):
        self.child = dict()
        self.words = list()
    def insert(self, word: str) -> None:
        cur = self
        for ch in word:
            if ch not in cur.child:
                cur.child[ch] = Trie()
            cur = cur.child[ch]
            cur.words.append(word)
            cur.words.sort()
            if len(cur.words) > 3: # 只保留前三個
                cur.words.pop()
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = Trie()
        for word in products:
            root.insert(word)
        ans = [[] for _ in range(len(searchWord))]
        cur = root
        for idx, ch in enumerate(searchWord):
            if ch in cur.child:
                cur = cur.child[ch]
                ans[idx] = cur.words
            else:
                break
        return ans

# @lc code=end

sol = Solution()
print(sol.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"],"mouse"))