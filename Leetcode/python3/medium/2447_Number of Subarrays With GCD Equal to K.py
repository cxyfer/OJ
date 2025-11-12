#
# @lc app=leetcode id=2447 lang=python3
#
# [2447] Number of Subarrays With GCD Equal to K
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
LogTrick

由於 gcd 的性質，以 r 為右端點的區間 gcd 值最多有 log U 種，其中 U = max(nums)。
因此可以維護以 r 為右端點的區間 gcd 值，對於同樣的 gcd 值合併出現次數。
"""
# @lc code=start
class Solution1:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i, x in enumerate(nums):
            g = 0
            for j in range(i, n):
                g = math.gcd(g, nums[j])
                if g % k != 0:
                    break
                if g == k:
                    ans += 1
        return ans

class Solution2:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ans = 0
        gcds = []  # (區間 gcd，出現次數)
        for r, x in enumerate(nums):
            # 維護以 r 為右端點的所有區間 gcd 值
            for p in gcds:
                p[0] = math.gcd(p[0], x)
            gcds.append([x, 1])

            # 原地去重，相同 gcd 值合併出現次數
            idx = 1
            for j in range(1, len(gcds)):
                if gcds[j][0] != gcds[idx - 1][0]:
                    gcds[idx] = gcds[j]
                    idx += 1
                else:
                    gcds[idx - 1][1] += gcds[j][1]
            del gcds[idx:]

            for g, c in gcds:
                if g == k:
                    ans += c
                    break
        return ans

Solution = Solution1
# Solution = Solution2
# @lc code=end

sol = Solution()
print(sol.subarrayGCD([9,3,1,2,6,3], 3))  # 4
print(sol.subarrayGCD([4], 7))  # 0