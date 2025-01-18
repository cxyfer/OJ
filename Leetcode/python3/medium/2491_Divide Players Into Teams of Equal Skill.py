#
# @lc app=leetcode id=2491 lang=python3
# @lcpr version=30204
#
# [2491] Divide Players Into Teams of Equal Skill
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()
        target = skill[0] + skill[-1]
        ans = 0
        for i in range(n // 2):
            if skill[i] + skill[n - i - 1] != target:
                return -1
            ans += skill[i] * skill[n - i - 1]
        return ans

class Solution2:
    def dividePlayers(self, skill: List[int]) -> int:
        m = len(skill) // 2
        s = sum(skill)
        if s % m != 0:
            return -1
        target = s // m
        cnt = Counter(skill)
        ans = 0
        for k, v in cnt.items():
            if cnt[target - k] != v:
                return -1
            ans += k * (target - k) * v
        return ans // 2

class Solution(Solution1): 
# class Solution(Solution2):
    pass
# @lc code=end



#
# @lcpr case=start
# [3,2,5,1,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2,3]\n
# @lcpr case=end

#

