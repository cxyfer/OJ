#
# @lc app=leetcode id=3327 lang=python3
# @lcpr version=30204
#
# [3327] Check if DFS Strings Are Palindromes
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Manacher:
    def __init__(self, s) -> None:
        self.s = s
        if isinstance(s, str):
            self.t = '#'.join(['^'] + list(s) + ['$'])
        elif isinstance(s, list):
            self.t = '#'.join(['^'] + s + ['$'])
        else:
            raise ValueError("s must be a string or a list")
        
        self.halfLen = [0] * (len(self.t) - 2)
        self.halfLen[1] = 1
        boxM = boxR = 0
        for i in range(2, len(self.halfLen)):
            hl = 1
            if i < boxR:
                hl = min(self.halfLen[boxM * 2 - i], boxR - i)
            while self.t[i - hl] == self.t[i + hl]:
                hl += 1
                boxM, boxR = i, i + hl
            self.halfLen[i] = hl

    # 判斷 s[l:r] 是否為回文字串
    def isPalindrome(self, l: int, r: int) -> bool:
        return self.halfLen[l + r + 1] > r - l

class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        n = len(parent)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parent[i]].append(i)

        dfsStr = [''] * n
        nodes = [[0, 0] for _ in range(n)] # (start, end)
        time = 0
        def dfs(x: int) -> None:
            nonlocal time
            nodes[x][0] = time
            for y in g[x]:
                dfs(y)
            dfsStr[time] = s[x]
            time += 1
            nodes[x][1] = time
            
        dfs(0)
        manacher = Manacher(dfsStr)
        return [manacher.isPalindrome(l, r) for l, r in nodes]
# @lc code=end

sol = Solution()
print(sol.findAnswer([-1,0,0,1,1,2], "aababa")) # [True, True, False, True, True, True]
print(sol.findAnswer([-1,0,0,0,0], "aabcb")) # [True, True, True, True, True]
#
# @lcpr case=start
# [-1,0,0,1,1,2]\n"aababa"\n
# @lcpr case=end

# @lcpr case=start
# [-1,0,0,0,0]\n"aabcb"\n
# @lcpr case=end

#

