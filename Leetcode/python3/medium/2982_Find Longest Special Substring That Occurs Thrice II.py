#
# @lc app=leetcode id=2982 lang=python3
# @lcpr version=30202
#
# [2982] Find Longest Special Substring That Occurs Thrice II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        1. Counter
          O(n + 26 * n)
        2. Sort
          O(n + 26 nlogn)
        3. Min Heap
          O(n log 3 + 26 * 3 log 3)
    """
    def maximumLength(self, s: str) -> int:
        # return self.solve1(s)
        return self.solve2(s)
        # return self.solve3(s)
    def solve1(self, s: str) -> int:
        n = len(s)
        # groups = [Counter() for _ in range(26)] # TLE
        groups = [[0] * (n+1) for _ in range(26)] # AC
        i = 0
        while i < n: # 分組循環
            st, i, idx = i, i+1, ord(s[i]) - ord("a")
            while (i < n and s[i] == s[st]):
                i += 1
            # for k in range(1, i - st + 1): # 長度為 k 的子字串有 i - st - k + 1 個
            for k in range(i - st, max(0, i - st - 3), -1): # 其實最多考慮 3 個就夠了
                groups[idx][k] += i - st - k + 1
        ans = -1
        for g in groups:
            # for i in range(n, 0, -1): 
            for i in range(n-2, 0, -1): # 需要出現至少 3 次
                if g[i] >= 3: # 滿足條件
                    ans = max(ans, i)
                    break
        return ans
    def solve2(self, s: str) -> int:
        n = len(s)
        groups = [[] for _ in range(26)]
        i = 0
        while i < n: # 分組循環
            st, i = i, i+1
            while (i < n and s[i] == s[st]):
                i += 1
            groups[ord(s[st]) - ord("a")].append(i - st)
        ans = 0
        for g in groups:
            m = len(g)
            if m == 0: continue
            g.sort(reverse=True)
            ans = max(ans, g[0]-2)
            if m > 1: ans = max(ans, min(g[0]-1, g[1]))
            if m > 2: ans = max(ans, g[2])
        return ans if ans > 0 else -1
    def solve3(self, s: str) -> int:
        n = len(s)
        groups = [[] for _ in range(26)]
        i = 0
        while i < n: # 分組循環
            st = i
            while (i < n and s[i] == s[st]):
                i += 1
            idx = ord(s[st]) - ord("a")
            if len(groups[idx]) >= 3:
                heappushpop(groups[idx], (i - st)) # Min heap
            else:
                heappush(groups[idx], (i - st)) # Min heap
        ans = 0
        for g in groups:
            m = len(g)
            if m == 0: continue
            tmp = [0] * 3
            for i in range(m-1, -1, -1):
                tmp[i] = heappop(g)
            ans = max(ans, tmp[0]-2, min(tmp[0]-1, tmp[1]), tmp[2])
        return ans if ans > 0 else -1
# @lc code=end

sol = Solution()
print(sol.maximumLength("aaaa")) # 2
print(sol.maximumLength("abcdef")) # -1
print(sol.maximumLength("abcaba")) # 1
print(sol.maximumLength("aada")) # 1
print(sol.maximumLength("ereerrrererrrererre")) # 2

#
# @lcpr case=start
# "aaaa"\n
# @lcpr case=end

# @lcpr case=start
# "abcdef"\n
# @lcpr case=end

# @lcpr case=start
# "abcaba"\n
# @lcpr case=end

#

