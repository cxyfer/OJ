#
# @lc app=leetcode.cn id=275 lang=python3
#
# [275] H 指数 II
#
from preImport import *
# @lc code=start
class Solution:
    """
        Binary search
        citations 已经按照升序排列，所以可以對答案的範圍進行二分查找
        Time: O(logn)

        注意循環不變量：
        - left - 1 的回答一定為「是」
        - right + 1 的回答一定為「否」
    """
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n # [left, right]
        while left <= right: # 區間不為空
            # 
            # right - 1 為「是」
            mid = (left + right) // 2
            if citations[-mid] >= mid: # 最高的 mid 篇論文引用次數皆 >= mid ?
                left = mid + 1
            else:
                right = mid - 1
        return right # or left - 1
# @lc code=end
sol = Solution()
print(sol.hIndex([0]))
citations = [0,1,3,5,6]
print(citations[-1])