#
# @lc app=leetcode id=995 lang=python3
# @lcpr version=30204
#
# [995] Minimum Number of K Consecutive Bit Flips
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start

"""
    3191. Minimum Operations to Make Binary Array Elements Equal to One I 的進階版
    由於 k <= n ，因此 3191 那樣的模擬操作需要 n^2 ，顯然是不可行的

    1. Differece Array
        把區間翻轉的操作轉換為差分陣列的操作
    2. Sliding Window

    要更快的話可以把次數改成二進制，這樣就不用每次都去判斷奇偶性質了。
"""
class Solution1:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0 # 總共的翻轉次數
        cur = 0 # 當前位置的翻轉次數，對 diff 陣列求前綴和得出
        diff = [0] * (n + 1) # 翻轉次數的差分陣列
        for i, x in enumerate(nums):
            cur += diff[i] # 求前綴和
            if x == cur & 1: # 需要翻轉
                if i + k > n: # 無法翻轉
                    return -1
                ans += 1
                cur += 1
                # 將 [i, i + k) 區間的翻轉次數加一
                diff[i] += 1 # 由於後續用不到了，其實可以省略
                diff[i + k] -= 1
        return ans

class Solution2:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0 # 總共的翻轉次數
        cur = 0 # 窗口內的翻轉次數
        for i in range(n):
            if i >= k: # 窗口有超過 k 個元素時才需要出窗口
                if nums[i - k] > 1: # i - k 位置被翻轉過，當前位置的翻轉次數時需要減一
                    cur -= 1
                    nums[i - k] -= 2 # 取消標記
            if nums[i] == (cur & 1): # 需要翻轉
                if i + k - 1 > n - 1: # 無法翻轉
                    return -1
                nums[i] += 2 # 標記這個位置，代表從這個位置開始的 k 個元素被翻轉過
                cur += 1
                ans += 1
        return ans
    
class Solution(Solution1):
# class Solution(Solution2):
    pass
# @lc code=end

sol = Solution()
print(sol.minKBitFlips([0,1,0], 1)) # 2
print(sol.minKBitFlips([1,1,0], 2)) # -1
print(sol.minKBitFlips([0,0,0,1,0,1,1,0], 3)) # 3

#
# @lcpr case=start
# [0,1,0]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,1,0]\n2\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0,1,0,1,1,0]\n3\n
# @lcpr case=end

#

