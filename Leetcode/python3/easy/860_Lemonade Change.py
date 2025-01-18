#
# @lc app=leetcode id=860 lang=python3
# @lcpr version=30204
#
# [860] Lemonade Change
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cnt5 = cnt10 = cnt20 = 0 # 硬幣數量
        for x in bills: # 支付的方式
            if x == 5: # 5元
                cnt5 += 1
            elif x == 10: # 10元
                cnt10 += 1
                cnt5 -= 1
            else: # 20元
                # cnt20 += 1 # 實際上不需要紀錄 20 元的數量
                if cnt10 > 0: # 如果有10元，就先找10元
                    cnt10 -= 1
                    cnt5 -= 1
                else: # 如果沒有10元，就找3個5元
                    cnt5 -= 3
            if cnt5 < 0: # 5 元硬幣不夠用，無法找零
                return False
        return True
# @lc code=end

#
# @lcpr case=start
# [5,5,5,10,20]\n
# @lcpr case=end

# @lcpr case=start
# [5,5,10,10,20]\n
# @lcpr case=end

#

