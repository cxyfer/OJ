#
# @lc app=leetcode id=2244 lang=python3
# @lcpr version=30201
#
# [2244] Minimum Rounds to Complete All Tasks
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        cnt = Counter(tasks)
        ans = 0
        for v in cnt.values():
            if v == 1:
                return -1
            # r = v % 3
            # if r == 1:
            #     ans += v // 3 + 1 # (v // 3 - 1) + 2
            # elif r == 2:
            #     ans += v // 3 + 1
            # else:
            #     ans += v // 3
            ans += v // 3 + (v % 3 != 0)
        return ans
# @lc code=end

sol = Solution()
print(sol.minimumRounds([5,5,5,5])) # 2
print(sol.minimumRounds([66,66,63,61,63,63,64,66,66,65,66,65,61,67,68,66,62,67,61,64,66,60,69,66,65,68,63,60,67,62,68,60,66,64,60,60,60,62,66,64,63,65,60,69,63,68,68,69,68,61])) # 20


#
# @lcpr case=start
# [2,2,3,3,2,4,4,4,4,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,3]\n
# @lcpr case=end

#

