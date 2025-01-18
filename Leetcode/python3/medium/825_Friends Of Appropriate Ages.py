#
# @lc app=leetcode id=825 lang=python3
# @lcpr version=30204
#
# [825] Friends Of Appropriate Ages
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        cnt = [0] * 121 # 每個年齡的人數
        for age in ages:
            cnt[age] += 1
        s = list(accumulate(cnt, initial=0))

        ans = 0
        for x, v in enumerate(cnt):
            if v == 0:
                continue
            mn = int(x * 0.5) + 8
            if mn > x:
                continue
            mx = x
            send = s[mx+1] - s[mn]
            ans += cnt[x] * (send - 1) # 減去自己
        return ans
# @lc code=end



#
# @lcpr case=start
# [16,16]\n
# @lcpr case=end

# @lcpr case=start
# [16,17,18]\n
# @lcpr case=end

# @lcpr case=start
# [20,30,100,110,120]\n
# @lcpr case=end

#

