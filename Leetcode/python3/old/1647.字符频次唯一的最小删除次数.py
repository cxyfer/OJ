#
# @lc app=leetcode.cn id=1647 lang=python3
#
# [1647] 字符频次唯一的最小删除次数
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def minDeletions(self, s: str) -> int:
        # cnt = Counter(Counter(s).values())
        # res = 0
        # while(any(cnt[k] > 1 for k in cnt.keys() if k > 0)): # 有重複
        #     for k in sorted(cnt.keys(), reverse=True):
        #         while cnt[k] > 1:
        #             cnt[k] -= 1
        #             cnt[k-1] += 1
        #             res += 1
        # return res
        cnt = Counter(s)
        check = set()
        res = 0
        for ch, val in cnt.items():
            cur = val
            while cur > 0 and cur in check: # 出現次數重複
                cur -= 1
            res += val - cur  # 刪除的次數
            if cur > 0:
                check.add(cur)
        return res
# @lc code=end

sol = Solution()
# print(sol.minDeletions("aab")) # 0
# print(sol.minDeletions("aaabbbcc")) # 2
# print(sol.minDeletions("ceabaacb")) # 2 
# print(sol.minDeletions("abcabc")) # 3
print(sol.minDeletions("bbcebab")) # 2
