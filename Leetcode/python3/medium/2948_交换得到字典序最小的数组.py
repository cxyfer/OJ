2#
# @lc app=leetcode.cn id=2948 lang=python3
#
# [2948] 交换得到字典序最小的数组
#
from preImport import *
# @lc code=start
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        ans = [0] * n

        lst = [(num, idx) for idx, num in enumerate(nums)]
        lst.sort()

        i = 0
        while i < n:
            num, idx = lst[i]
            hp_idx = []
            hp_num = []
            heappush(hp_idx, idx)
            heappush(hp_num, num)
            j = i + 1
            while j < n and lst[j][0] - lst[j-1][0] <= limit:
                heappush(hp_idx, lst[j][1])
                heappush(hp_num, lst[j][0])
                j += 1
            # print(i, j, lst[i:j])
            # print(hp_idx, hp_num)
            while hp_idx:
                ans[heappop(hp_idx)] = heappop(hp_num)
            i = j
        return ans
# @lc code=end

