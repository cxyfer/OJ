#
# @lc app=leetcode id=522 lang=python3
# @lcpr version=30203
#
# [522] Longest Uncommon Subsequence II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSubsequence(s: str, t: str) -> bool:
            i, j = 0, 0
            while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    i += 1
                j += 1
            return i == len(s)
        ans = -1
        for i, s in enumerate(strs):
            for j, t in enumerate(strs):
                if i != j and isSubsequence(s, t):
                    break
            else:
                ans = max(ans, len(s))
        return ans
    
class Solution2:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSubsequence(s: str, t: str) -> bool:
            i, j = 0, 0
            while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    i += 1
                j += 1
            return i == len(s)
        strs.sort(key=lambda x: len(x), reverse=True)
        for i, s in enumerate(strs):
            for j, t in enumerate(strs):
                if i != j and isSubsequence(s, t):
                    break
            else:
                return len(s)
        return -1
    
class Solution3:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSubsequence(s: str, t: str) -> bool:
            i, j = 0, 0
            while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    i += 1
                j += 1
            return i == len(s)
        cnt = Counter(strs)
        strs = list(cnt.keys())
        uniques = [s for s, v in cnt.items() if v == 1]
        uniques.sort(key=lambda x: len(x), reverse=True)
        for s in uniques:
            for t in strs:
                if s != t and isSubsequence(s, t):
                    break
            else:
                return len(s)
        return -1
# class Solution(Solution1):
#     pass
# class Solution(Solution2):
#     pass
class Solution(Solution3):
    pass
# @lc code=end

sol = Solution()
["aba","cdc","eae"]
print(sol.findLUSlength(["aba","cdc","eae"])) # 3

#
# @lcpr case=start
# ["aba","cdc","eae"]\n
# @lcpr case=end

# @lcpr case=start
# ["aaa","aaa","aa"]\n
# @lcpr case=end

#

