#
# @lc app=leetcode id=140 lang=python3
# @lcpr version=30202
#
# [140] Word Break II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Node: # Trie Node
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # return self.solve1(s, wordDict)
        # return self.solve2(s, wordDict)
        # return self.solve3a(s, wordDict)
        return self.solve3b(s, wordDict)
    """
        1. 劃分型DP + Memoization + Hash Table
        但返回的不是劃分的數量，而是劃分的結果
    """
    def solve1(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        wordSet = set(wordDict)
        @cache # Memoization
        def dfs(i: int) -> List[List[str]]: # 返回 s[i:] 的所有可能劃分
            if i == n:
                return [[]]
            res = []
            for j in range(i, n): # 枚舉當前單字的結尾位置
                if s[i:j+1] in wordSet:
                    for words in dfs(j + 1):
                        res.append([s[i:j + 1]] + words)
            return res
        return [' '.join(words) for words in dfs(0)] # 將劃分的結果轉為字串
    
    """
        2. Backtracking + Trie
    """
    def solve2(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        root = Node() # Trie
        for word in wordDict:
            cur = root
            for ch in word:
                idx = ord(ch) - ord('a')
                if cur.children[idx] is None:
                    cur.children[idx] = Node()
                cur = cur.children[idx]
            cur.isEnd = True # 標記當前 Trie 節點是某個單字的結尾
        ans = []
        path = []
        def dfs(i: int, cur: Node, word: str) -> None: # Backtracking
            if i == n:
                if cur == root:
                    ans.append(" ".join(path))
                return
            idx = ord(s[i]) - ord('a')
            if cur.children[idx] is None: # 如果當前字元不在 Trie 中，則直接返回 (剪枝)
                return
            word += s[i] # 當前字元加入 word
            nxt = cur.children[idx]
            dfs(i + 1, nxt, word) # 不劃分，繼續往下找
            if nxt.isEnd: # 當前字元是單字的結尾，可以劃分
                path.append(word)
                dfs(i + 1, root, "") # 劃分，繼續從 Trie 的根節點開始
                path.pop()
        dfs(0, root, "")
        return ans
    """
        3. Backtracking 枚舉劃分點
        https://leetcode.cn/problems/word-break-ii/solutions/1949490/gong-shui-san-xie-by-ac_oier-5xrk/
    """
    def solve3a(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        wordSet = set(wordDict)
        ans = []
        for i in range(0, 1 << (n - 1)): # 枚舉所有劃分點形成的子集合
            res = ""
            k = -1 # 最後一個劃分點在 res 中的位置
            for j in range(n):
                res += s[j]
                if i & (1 << j) or j == n - 1: # 在 s[j] 之後要劃分
                    if res[k+1:] not in wordSet: # 無效劃分
                        break
                    if j != n - 1:
                        res += " "
                    k = len(res) - 1 # 更新最後一個劃分點在 res 中的位置
            else:
                ans.append(res)
        return ans
    def solve3b(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        wordSet = set(wordDict)
        ans = []
        for i in range(0, 1 << (n - 1)): # 枚舉所有劃分點形成的子集合
            path = [] # 劃分結果
            word = "" # 當前單字
            for j in range(n):
                word += s[j]
                if i & (1 << j) or j == n - 1: # 在 s[j] 之後要劃分
                    if word not in wordSet: # 無法劃分
                        break
                    path.append(word)
                    word = ""
            else:
                ans.append(" ".join(path))
        return ans
# @lc code=end

sol = Solution()
print(sol.wordBreak("catsanddog", ["cat","cats","and","sand","dog"])) 


#
# @lcpr case=start
# "catsanddog"\n["cat","cats","and","sand","dog"]\n
# @lcpr case=end

# @lcpr case=start
# "pineapplepenapple"\n["apple","pen","applepen","pine","pineapple"]\n
# @lcpr case=end

# @lcpr case=start
# "catsandog"\n["cats","dog","sand","and","cat"]\n
# @lcpr case=end

#

