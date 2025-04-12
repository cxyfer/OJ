#
# @lc app=leetcode id=3272 lang=python3
#
# [3272] Find the Count of Good Integers
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
fact = [1]
for i in range(1, 11):
    fact.append(fact[-1] * i)

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        vis = set()
        base = 10 ** ((n - 1) // 2)
        for i in range(base, base * 10):
            s = str(i)
            s += s[::-1][n & 1:]
            x = int(s)
            if x % k:
                continue
            vis.add("".join(sorted(s)))

        ans = 0
        for s in vis:
            cnt = [0] * 10
            for ch in s:
                cnt[int(ch)] += 1
            cur = (n - cnt[0]) * fact[n - 1]
            for x in cnt:
                cur //= fact[x]
            ans += cur
        return ans
# @lc code=end

