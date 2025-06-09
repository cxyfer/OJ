#
# @lc app=leetcode id=3579 lang=python3
#
# [3579] Minimum Steps to Convert String with Operations
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minOperations(self, word1: str, word2: str) -> int:
        n = len(word1)

        def cost(s1: str, s2: str, reverse: bool):
            res = 0
            if reverse:
                s1 = reversed(s1)
                res += 1
            cnt = defaultdict(int)
            for x, y in zip(s1, s2):
                if x == y:
                    continue
                if cnt[(y, x)] > 0:
                    cnt[(y, x)] -= 1
                else:
                    cnt[(x, y)] += 1
                    res += 1
            return res
        
        @cache
        def f(i: int) -> int:
            if i == n:
                return 0
            res = float("inf")
            for j in range(i, n):
                res = min(res, f(j + 1) + min(cost(word1[i:j + 1], word2[i:j + 1], False), cost(word1[i:j + 1], word2[i:j + 1], True)))
            return res
        return f(0)
# @lc code=end

