#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # Merge 3 sorted list
        p = p2 = p3 = p5 = 1 # Pointers
        ugly = [0]
        res2 = res3 = res5 = 1
        while p <= n:
            min_ugly = min(res2, res3, res5)
            ugly.append(min_ugly)
            p += 1
            if min_ugly == res2:
                res2 = ugly[p2] * 2
                p2 += 1
            if min_ugly == res3:
                res3 = ugly[p3] * 3
                p3 += 1
            if min_ugly == res5:
                res5 = ugly[p5] * 5
                p5 += 1
        return ugly[n]

# @lc code=end

