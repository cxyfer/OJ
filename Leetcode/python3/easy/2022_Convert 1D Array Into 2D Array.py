#
# @lc app=leetcode id=2022 lang=python3
# @lcpr version=30204
#
# [2022] Convert 1D Array Into 2D Array
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        z = len(original)
        if z != m * n:
            return []
        return [[original[i * n + j] for j in range(n)] for i in range(m)]
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n2\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n1\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n1\n1\n
# @lcpr case=end

#

