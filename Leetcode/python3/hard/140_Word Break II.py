#
# @lc app=leetcode id=140 lang=python3
# @lcpr version=30202
#
# [140] Word Break II
#


# @lcpr-template-start
from preImport import *

# @lcpr-template-end
"""
1. 劃分型DP + Memoization + Hash Table
但返回的不是劃分的數量，而是劃分的結果

2. Backtracking + Trie

3. Backtracking 枚舉劃分點
https://leetcode.cn/problems/word-break-ii/solutions/1949490/gong-shui-san-xie-by-ac_oier-5xrk/
"""


# @lc code=start
class Solution1:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        wordSet = set(wordDict)

        @cache  # Memoization
        def dfs(i: int) -> List[List[str]]:  # 返回 s[i:] 的所有可能劃分
            if i == n:
                return [[]]  # 劃分完成，返回一個空的劃分結果
            res = []
            for j in range(i, n):  # 枚舉當前單字的結尾位置
                word = s[i : j + 1]
                if word in wordSet:
                    for words in dfs(j + 1):
                        res.append([word] + words)
            return res

        return [" ".join(words) for words in dfs(0)]  # 將劃分的結果轉為字串


class TrieNode:  # Trie Node
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False


class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        root = TrieNode()  # Trie
        for word in wordDict:
            node = root
            for ch in word:
                c = ord(ch) - ord("a")
                if node.children[c] is None:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.isEnd = True  # 標記當前 Trie 節點是某個單字的結尾

        ans = []
        path = []

        def dfs(i: int, node: TrieNode, word: str) -> None:  # Backtracking
            if i == n:
                if node == root:
                    ans.append(" ".join(path))
                return
            c = ord(s[i]) - ord("a")
            if node.children[c] is None:  # 如果當前字元不在 Trie 中，則直接返回 (剪枝)
                return
            word += s[i]  # 當前字元加入 word
            node = node.children[c]

            # 1. 不劃分，繼續往下找
            dfs(i + 1, node, word)

            # 2. 如果當前字元是單字的結尾，可以劃分
            if node.isEnd:
                path.append(word)
                dfs(i + 1, root, "")  # 繼續從 Trie 的根節點開始
                path.pop()

        dfs(0, root, "")
        return ans


class Solution3:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        wordSet = set(wordDict)
        ans = []
        for i in range(0, 1 << (n - 1)):  # 枚舉所有劃分點形成的子集合
            path = []  # 劃分結果
            st = 0  # 當前單字的起始位置
            for j in range(n):
                if i & (1 << j) or j == n - 1:  # 在 s[j] 之後要劃分
                    word = s[st : j + 1]  # 當前單字
                    st = j + 1  # 更新下一個單字的起始位置
                    if word not in wordSet:  # 無法劃分
                        break
                    path.append(word)
            else:
                ans.append(" ".join(path))
        return ans


# Solution = Solution1
# Solution = Solution2
Solution = Solution3
# @lc code=end

sol = Solution()
print(sol.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))


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
