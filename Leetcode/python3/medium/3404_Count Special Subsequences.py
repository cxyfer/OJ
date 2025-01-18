#
# @lc app=leetcode id=3404 lang=python3
# @lcpr version=30204
#
# [3404] Count Special Subsequences
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
gcds = [[math.gcd(i, j) for j in range(1001)] for i in range(1001)]
def gcd(a, b):
    return gcds[a][b]

class Solution:
    """
       nums[p] * nums[r] = nums[q] * nums[s]
    => nums[p] / nums[q] = nums[s] / nums[r]
    """
    def numberOfSubsequences(self, nums: List[int]) -> int:
        n = len(nums)
        
        suf = defaultdict(int)
        for r in range(4, n - 2):
            r_val = nums[r]
            for s in range(r + 2, n):
                s_val = nums[s]
                g = gcd(r_val, s_val)
                suf[s_val // g, r_val // g] += 1

        ans = 0
        for q in range(2, n - 4):
            q_val = nums[q]
            for p in range(q - 2, -1, -1):
                p_val = nums[p]
                g = gcd(p_val, q_val)
                ans += suf[p_val // g, q_val // g]

            r = q + 2
            r_val = nums[r]
            for s in range(r + 2, n):
                s_val = nums[s]
                g = gcd(r_val, s_val)
                suf[s_val // g, r_val // g] -= 1
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,3,6,1]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,3,4,3,4,3,4]\n
# @lcpr case=end

#

