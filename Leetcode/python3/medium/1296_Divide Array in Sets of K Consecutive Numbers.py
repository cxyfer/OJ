#
# @lc app=leetcode id=1296 lang=python3
# @lcpr version=30203
#
# [1296] Divide Array in Sets of K Consecutive Numbers
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        cnt = Counter(nums)
        for x in sorted(cnt.keys()):
            if cnt[x] == 0:
                continue
            need = cnt[x]
            for i in range(k):
                if cnt[x+i] < need:
                    return False
                cnt[x+i] -= need
        return True
# @lc code=end



#
# @lcpr case=start
# [1,2,3,3,4,4,5,6]\n4\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1,2,3,4,3,4,5,9,10,11]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n3\n
# @lcpr case=end

#

