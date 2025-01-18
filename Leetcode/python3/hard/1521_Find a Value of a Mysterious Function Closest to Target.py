#
# @lc app=leetcode id=1521 lang=python3
# @lcpr version=30203
#
# [1521] Find a Value of a Mysterious Function Closest to Target
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        Same to 3171. Find Subarray With Bitwise AND Closest to K
        AND 只會讓數字變小，所以可以用 Stack 來保存所有可能的 AND 結果
    """
    def closestToTarget(self, arr: List[int], target: int) -> int:
        n = len(arr)
        ans = float("inf")
        st = []
        for x in arr:
            st2 = [x]
            for y in st:
                if y & x != st2[-1]:
                    st2.append(y & x)
            st = st2
            for y in st:
                ans = min(ans, abs(y - target))
        return ans
# @lc code=end



#
# @lcpr case=start
# [9,12,3,7,15]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1000000,1000000,1000000]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2,4,8,16]\n0\n
# @lcpr case=end

#

