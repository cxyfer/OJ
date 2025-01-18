#
# @lc app=leetcode.cn id=1964 lang=python3
#
# [1964] 找出到每个位置为止最长的有效障碍赛跑路线
#
from preImport import *
# @lc code=start
class Solution:
    """
        Longest Increasing Subsequence (LIS)
        1 <= obstacles[i] <= 10e7
        -> O(n^2) 會 TLE，需要用到二分查找
    """
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        ans = [1] * n
        tail = [obstacles[0]] # tail[i] 表示 長度為 i+1 的 LIS 的最後一個元素的最小值，初始化 tail[0] = nums[0]
        for i in range(1, n):
            if obstacles[i] >= tail[-1]: # nums[i] 可以接在 tail 的末尾，並構成更長的 LIS
                tail.append(obstacles[i]) # tail 長度加 1
                ans[i] = len(tail)
                continue

            # 在 tail 中二分查找，找到第一個 > nums[i] 的元素，並將其更新為 nums[i]
            j = bisect_right(tail, obstacles[i])
            tail[j] = obstacles[i]
            ans[i] = j + 1 # 以 nums[i] 結尾的 LIS 長度為 j+1
        return ans
# @lc code=end
sol = Solution()
print(sol.longestObstacleCourseAtEachPosition([1,2,3,2])) # [1,2,3,3]
print(sol.longestObstacleCourseAtEachPosition([2,2,1])) # [1,2,1]
print(sol.longestObstacleCourseAtEachPosition([3,1,5,6,4,2])) # [1,1,2,3,2,2]