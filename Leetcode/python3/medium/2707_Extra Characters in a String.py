#
# @lc app=leetcode id=2707 lang=python3
# @lcpr version=30204
#
# [2707] Extra Characters in a String
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        words = set(dictionary)
        
        # 從第 i 個位置開始，所得到的獨立字元數 
        @cache # Memoization
        def dfs(i: int):
            if i >= n:
                return 0
            res = dfs(i + 1) + 1 # 不選，即第 i 個字元為獨立字元的情況
            for j in range(i, n): # 枚舉以第 i 個字元開頭的字
                if s[i:j+1] in words: # 如果該字串在字典中
                    res = min(res, dfs(j+1)) # 選擇該字串，並遞迴計算剩餘字串的獨立字元數
            return res
        return dfs(0)

class TrieNode:
    def __init__(self) -> None:
        self.child = {}
        self.is_end = False

class Solution2:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)

        root = TrieNode()
        for word in dictionary:
            node = root
            for ch in word:
                if ch not in node.child:
                    node.child[ch] = TrieNode()
                node = node.child[ch]
            node.is_end = True
        
        @cache
        def dfs(i: int):
            if i >= n:
                return 0
            res = dfs(i + 1) + 1 # 不選，即第 i 個字元為獨立字元的情況
            node = root
            for j in range(i, n):
                ch = s[j]
                if ch not in node.child: # 當前字元不在字典樹中，不用繼續往下找
                    break
                node = node.child[ch]
                if node.is_end: # 選，s[i:j+1] 在字典中
                    res = min(res, dfs(j + 1))
            return res
        return dfs(0)
    
class Solution(Solution1):
    pass
# @lc code=end



#
# @lcpr case=start
# "leetscode"\n["leet","code","leetcode"]\n
# @lcpr case=end

# @lcpr case=start
# "sayhelloworld"\n["hello","world"]\n
# @lcpr case=end

#

