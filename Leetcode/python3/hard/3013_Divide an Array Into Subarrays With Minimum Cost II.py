#
# @lc app=leetcode id=3013 lang=python3
#
# [3013] Divide an Array Into Subarrays With Minimum Cost II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
題意等同於在大小為 dist + 1 的 window 中，找到最小的 k - 1 個數
這可以用類似 480. Sliding Window Median 的方式維護一組有序列表 L 和 R，
使得 L[-1] <= R[0]，且 L 的大小為 k - 1

注意在入窗口時不能無腦地將 nums[r] 加入 L，這可能導致 L[-1] > R[0]
"""
# @lc code=start
from sortedcontainers import SortedList

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        L = SortedList(nums[1:dist + 2])
        R = SortedList()
        s = sum(nums[:dist + 2])
        k -= 1

        def L2R() -> None:
            nonlocal s
            x = L.pop()  # 把 L 的最大值加入 R
            s -= x
            R.add(x)

        def R2L() -> None:
            nonlocal s
            x = R.pop(0)  # 把 R 的最小值加入 L
            L.add(x)
            s += x

        while len(L) > k:  # 維護 L 的大小
            L2R()

        ans = s
        for r in range(dist + 2, n):
            # 1. 入窗口
            x = nums[r]
            if x <= L[-1]:
                L.add(x)
                s += x
            else:
                R.add(x)

            # 2. 出窗口
            y = nums[r - dist - 1]
            if y in L:
                L.remove(y)
                s -= y
            else:
                R.remove(y)

            # 3. 維護 L 的大小，這裡 L 的大小只會有 k + 1, k, k - 1 三種情況
            if len(L) > k:
                L2R()
            elif len(L) < k:
                R2L()

            # 4. 更新答案
            ans = min(ans, s)
        return ans
# @lc code=end

sol = Solution()
print(sol.minimumCost([10,8,18,9], 3, 1))  # 36
nums = [36,28,42,36,39,13,24,3,32,16,11,43,21,40,34,49,29,20,34,34,8,3,41,6,46,5,35,5,47,2]
print(sol.minimumCost(nums, 25, 26))  # 570