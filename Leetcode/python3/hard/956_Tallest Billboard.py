#
# @lc app=leetcode id=956 lang=python3
#
# [956] Tallest Billboard
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
Similar
- 3877. Minimum Removals to Achieve Target XOR
"""
# @lc code=start
class Solution1:
    def tallestBillboard(self, rods: List[int]) -> int:
        # 令 h1 表示支架 1 的高度，h2 表示支架 2 的高度， d = h1 - h2
        # f[d] 表示當 h1 - h2 = d 時，h1 的最大值
        f = defaultdict(int)
        f[0] = 0
        for x in rods:
            nf = f.copy()
            for d, h in f.items():
                nf[d + x] = max(nf[d + x], h + x)  # 分配給 h1
                nf[d - x] = max(nf[d - x], h)  # 分配給 h2
                # nf[d] = max(nf[d], h)  # 不分配，但已經包含在 f.copy() 內了
            f = nf
        return f[0]


class Solution2:
    def tallestBillboard(self, rods: List[int]) -> int:
        n = len(rods)
        mid = (n + 1) // 2

        def build(rods: list[int]) -> defaultdict:
            # 定義同 Solution1
            f = defaultdict(int)
            f[0] = 0
            for x in rods:
                nf = f.copy()
                for d, h in f.items():
                    nf[d + x] = max(nf[d + x], h + x)
                    nf[d - x] = max(nf[d - x], h)
                f = nf
            return f

        # Meet in the middle
        L = build(rods[:mid])
        R = build(rods[mid:])
        ans = 0
        # 當 h1_l - h2_l = d 時，需要找到 h1_r - h2_r = -d 的情況，
        # 才能讓 h1_l + h1_r = h2_l + h2_r，此時可以得到的最大 h1 = L[d] + R[-d]
        for d, h in L.items():
            if -d in R:
                ans = max(ans, h + R[-d])
        return ans


# Solution = Solution1
Solution = Solution2
# @lc code=end

sol = Solution()
print(sol.tallestBillboard([1,2,3,6]))  # 6
