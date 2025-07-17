#
# @lc app=leetcode id=3202 lang=python3
#
# [3202] Find the Maximum Length of Valid Subsequence II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. 枚舉 (sub[0] + sub[1]) % k 的值 s
令 f[i][j] 表示考慮前 i 個數，任兩項和為 s 時，最後一項 mod k 為 j 時的最大長度。
由於從 f[i - 1] 轉移到 f[i] 時，只依賴於 f[i - 1] 的狀態，可以用滾動的方式壓縮維度，
且由於只需要多考慮最後一項為 x = nums[i] % k 的情況，因此除了 f[i][x] 之外，其餘的值都和 f[i - 1] 相同。

又因為子序列中一定是 x, y, x, y 交錯，因此在選或不選 nums[i] 的兩種情況中，選一定不會比不選差，但這種寫法中就算不沒注意到這點也能通過。

2. 紀錄最後兩項
首先要注意到，子序列中一定是 x, y, x, y 交錯，因此只需要紀錄最後兩項即可。
令 f[i][y][x] 表示考慮前 i 個數，最後兩項 mod k 為 y, x 時的最大長度。
同樣地，由於從 f[i - 1] 轉移到 f[i] 時，只依賴於 f[i - 1] 的狀態，可以用滾動的方式壓縮維度，
且由於只需要多考慮最後一項為 x = nums[i] % k 的情況，因此除了 f[i][y][x] 之外，其餘的值都和 f[i - 1] 相同。
類似地，因此在選或不選 nums[i] 的兩種情況中，選一定不會比不選差。
"""
# @lc code=start
fmax = lambda x, y: x if x > y else y
class Solution1:
    def maximumLength(self, nums: List[int], k: int) -> int:
        nums[:] = [x % k for x in nums]
        ans = 0
        # 枚舉 (sub[0] + sub[1]) % k 的值
        for s in range(k):
            f = [0] * k
            for x in nums:
                # f[x] = fmax(f[x], f[(s - x) % k] + 1)  # 選或不選 nums[i]
                f[x] = f[(s - x) % k] + 1  # 但選了一定不會比不選差
            ans = fmax(ans, max(f))
        return ans

class Solution2:
    def maximumLength(self, nums: List[int], k: int) -> int:
        f = [[0] * k for _ in range(k)]
        for x in map(lambda x: x % k, nums):
            for y in range(k):
                f[y][x] = f[x][y] + 1
        return max(map(max, f))

Solution = Solution1  
# Solution = Solution2
# @lc code=end
# @lc code=end