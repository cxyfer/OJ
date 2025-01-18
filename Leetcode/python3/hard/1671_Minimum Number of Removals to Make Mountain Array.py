#
# @lc app=leetcode id=1671 lang=python3
# @lcpr version=30204
#
# [1671] Minimum Number of Removals to Make Mountain Array
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    LIS + 前後綴分解
"""
class Solution1:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        # 1. Find LIS from left to right
        pre = [1] * n # pre[i] 表示以 nums[i] 結尾的 LIS 長度
        for i in range(1, n): # 枚舉所有位置 i
            for j in range(i): # 枚舉 i 前面的所有位置 j
                if nums[i] > nums[j]: # nums[i] 可以接在 nums[j] 後面
                    pre[i] = max(pre[i], pre[j] + 1)

        # 2. Find LDS from right to left
        suf = [1] * n # suf[i] 表示以 nums[i] 為開頭的 LDS 長度
        for i in range(n-2, -1, -1):
            for j in range(n-1, i, -1):
                if nums[i] > nums[j]: # nums[i] 可以接在 nums[j] 前面
                    suf[i] = max(suf[i], suf[j] + 1)
    
        # 3. Find the maximum length of mountain array
        max_len = 0
        for i in range(1, n-1): # 以 i 為山頂
            # 若 pre[i] == 1 或 suf[i] == 1 代表山頂前或後沒有比它小的數字，根據定義，不是山形陣列
            if pre[i] > 1 and suf[i] > 1:
                max_len = max(max_len, pre[i] + suf[i] - 1) # 扣除重複的山頂
        return n - max_len
    
class Solution2:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)

        # pre[i] 表示以 nums[i] 結尾的 LIS 長度
        pre = [-1] * n
        tail = [] # tail[i] 表示長度為 i+1 的 LIS 的最後一個元素的最小值
        for i, x in enumerate(nums):
            j = bisect_left(tail, x) # 找到第一個 >= x 的元素位置
            if j == len(tail): # 如果 x 比 tail 中的所有元素都大，則將 x 添加到 tail 中
                tail.append(x)
            else: # 否則，更新 tail[j] 為 x
                tail[j] = x
            pre[i] = j + 1

        # suf[i] 表示以 nums[i] 為開頭的 LDS 長度
        # 這裡其實就只是反向求 LIS 而已，也可以透過反轉 nums 後求 LIS，並把結果再反轉回來
        suf = [-1] * n
        head = [] # head[i] 表示長度為 i+1 的 LDS 的第一個元素的最小值
        for i in range(n - 1, -1, -1):
            x = nums[i]
            j = bisect_left(head, x)
            if j == len(head):
                head.append(x)
            else:
                head[j] = x
            suf[i] = j + 1

        max_len = 0
        for i in range(n):
            if pre[i] > 1 and suf[i] > 1:
                max_len = max(max_len, pre[i] + suf[i] - 1)
        return n - max_len
# class Solution(Solution1):
class Solution(Solution2):
    pass
# @lc code=end

sol = Solution()
print(sol.minimumMountainRemovals([1,3,1])) # 0
print(sol.minimumMountainRemovals([2,1,1,5,6,2,3,1])) # 3
print(sol.minimumMountainRemovals([1,2,3,4,4,3,2,1])) # 1
print(sol.minimumMountainRemovals([9,8,1,7,6,5,4,3,2,1])) # 2

print(sol.minimumMountainRemovals([4,3,2,1,1,2,3,1])) # 4

#
# @lcpr case=start
# [1,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,1,5,6,2,3,1]\n
# @lcpr case=end

#

