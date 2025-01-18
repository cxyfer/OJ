#
# @lc app=leetcode.cn id=2386 lang=python3
#
# [2386] 找出数组的第 K 大和
#
from preImport import *
# @lc code=start
class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = 0 # 紀錄非負數的總和，即第1大和
        for i, x in enumerate(nums):
            if x >= 0:
                s += x
            else: # 使負數變成正數，要使第1大和變小可以加上負數或減去正數，這裡讓負數變成正數，使後面可以統一用減法
                nums[i] = -x
        nums.sort() # 由小到大排序

        ret = 0 # 要去除的元素和，初始化為0
        hp = [(nums[0], 0)] # (要去除的元素和, 已經考慮到的元素下標)，第一個考慮要去除的元素顯然是最小的元素
        for _ in range(2, k + 1):
            t, i = heappop(hp)
            ret = t
            if i == n - 1:
                continue
            heappush(hp, (t + nums[i + 1], i + 1)) # 保留nums[i]，加入nums[i+1]
            heappush(hp, (t - nums[i] + nums[i + 1], i + 1)) # 去除nums[i]，加入nums[i+1]
        return s - ret
# @lc code=end

