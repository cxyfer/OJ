#
# @lc app=leetcode id=2333 lang=python3
#
# [2333] Minimum Sum of Squared Difference
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        # 對 nums1 做 +1 操作的貢獻，等同於對 nums2 做 -1 操作的貢獻，反之亦然。
        # 因此可以將 k1 和 k2 的兩種操作視為同一種，並只保留 nums1 和 nums2 的差值。
        diff = [abs(x - y) for x, y in zip(nums1, nums2)]
        k = k1 + k2
        diff.sort(reverse=True)

        # 基於貪心的策略，每次操作選擇差值最大的位置操作對答案的貢獻最大。
        # 但顯然逐個操作會超時，因此可以換個角度思考，對相同的差值進行批量操作。
        # 例如對於差值為 x 的前 i 個元素，考慮能否將它們都減成下一個差值 y，如果可以，則又回到相同的問題。
        i = 0
        while i < n:
            x = diff[i]
            while i + 1 < n and diff[i] == diff[i + 1]:
                i += 1
            i += 1
            # 此時前 i 個都是 x，考慮能不能都減成下一個數 y
            y = diff[i] if i < n else 0
            if k > i * (x - y):
                k -= i * (x - y)
            else:
                q, r = divmod(k, i)
                x -= q
                # 此時有 r 個 x - 1、 i - r 個 x，剩下的元素不變，直接計算答案即可
                ans = x * x * (i - r) + (x - 1) * (x - 1) * r
                while i < n:
                    ans += diff[i] * diff[i]
                    i += 1
                return ans
        return 0
# @lc code=end

