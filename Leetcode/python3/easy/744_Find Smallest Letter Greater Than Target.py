#
# @lc app=leetcode id=744 lang=python3
# @lcpr version=30204
#
# [744] Find Smallest Letter Greater Than Target
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return letters[left] if left < n else letters[0]
        
# @lc code=end



#
# @lcpr case=start
# ["c","f","j"]\n"a"\n
# @lcpr case=end

# @lcpr case=start
# ["c","f","j"]\n"c"\n
# @lcpr case=end

# @lcpr case=start
# ["x","x","y","y"]\n"z"\n
# @lcpr case=end

#

