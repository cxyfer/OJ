#
# @lc app=leetcode.cn id=1287 lang=python3
#
# [1287] 有序数组中出现次数超过25%的元素
#
from preImport import *
# @lc code=start
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # return Counter(arr).most_common(1)[0][0]
        n = len(arr)
        span = n // 4 + 1 # 每隔 span 個元素檢查一次
        for i in range(0, n, span):
            l = bisect_left(arr, arr[i])
            r = bisect_right(arr, arr[i])
            if r - l >= span:
                return arr[i]
        return -1
# @lc code=end

