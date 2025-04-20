#
# @lc app=leetcode id=781 lang=python3
#
# [781] Rabbits in Forest
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # cnt = Counter(answers)
        # ans = 0
        # for k, v in cnt.items():
        #     sz = k + 1
        #     ans += sz * math.ceil(v / sz)
        # return ans
        return sum((k + 1) * math.ceil(v / (k + 1)) for k, v in Counter(answers).items())
# @lc code=end

