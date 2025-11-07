#
# @lc app=leetcode id=2528 lang=python3
#
# [2528] Maximize the Minimum Powered City
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
最大化最小值問題，可以使用二分搜尋來解決，難點在如何寫 check 函數。
在不增加發電廠的情況下，可以使用滑動窗口來維護 [i - d, i + d] 區間的和，如果和小於 mid，則需要增加發電廠。
如果在所有 j < i 的位置都已經滿足，則基於一點貪心思路，在 i + d 的位置增加發電廠是最優的。
注意到在 i + d 位置增加一個發電廠等同於在 [i, i + 2d] 區間增加一單位的電量，因此可以使用差分陣列來維護增加量。
"""
# @lc code=start
class Solution:
    def maxPower(self, stations: List[int], d: int, k: int) -> int:
        n = len(stations)

        def check(mid: int) -> bool:
            # 差分陣列 + 滑動窗口
            diff = [0] * (n + 1)  
            s = sum(stations[:d])
            cnt = 0
            for i in range(n):
                if (r := i + d) < n:
                    s += stations[r]
                if (l := i - d - 1) >= 0:
                    s -= stations[l]
                s += diff[i]
                if s < mid:
                    add = mid - s
                    cnt += add
                    if cnt > k:
                        return False
                    s += add
                    # 加在 i + d 的位置，當 i' = i + 2 * d + 1 的時候，需要減去 add
                    diff[min(n, i + 2 * d + 1)] -= add
            return True

        left = min(stations)
        right = sum(stations) + k
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right
# @lc code=end

sol = Solution()
print(sol.maxPower([1,2,4,5,0], 1, 2)) # 5
print(sol.maxPower([4,4,4,4], 0, 3)) # 4
print(sol.maxPower([13,12,8,14,7], 2, 23)) # 52
print(sol.maxPower([48,16,29,41,2,43,23], 5, 40)) # 194