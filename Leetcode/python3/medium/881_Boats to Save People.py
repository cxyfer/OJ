#
# @lc app=leetcode id=881 lang=python3
# @lcpr version=30203
#
# [881] Boats to Save People
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        people.sort()
        i, j = 0, len(people) - 1
        while i <= j:
            if people[i] + people[j] > limit: # 只能帶比較重的那一個人
                j -= 1
            else: # 可以帶兩個人
                i += 1
                j -= 1
            ans += 1
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [3,2,2,1]\n3\n
# @lcpr case=end

# @lcpr case=start
# [3,5,3,4]\n5\n
# @lcpr case=end

#

