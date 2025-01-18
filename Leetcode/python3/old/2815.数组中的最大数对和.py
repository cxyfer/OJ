#
# @lc app=leetcode.cn id=2815 lang=python3
#
# [2815] 数组中的最大数对和
#

# @lc code=start
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        dict = {}
        for num in nums: 
            if max(str(num)) not in dict:
                dict[max(str(num))] = [num]
            else:
                dict[max(str(num))].append(num)
        result = -1
        for selects in dict.values():
            if len(selects) > 1:
                selects.sort(reverse = True)
                result = max(result, selects[0] + selects[1])
        return result

# @lc code=end

