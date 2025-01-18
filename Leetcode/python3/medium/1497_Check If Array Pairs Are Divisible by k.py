#
# @lc app=leetcode id=1497 lang=python3
# @lcpr version=30204
#
# [1497] Check If Array Pairs Are Divisible by k
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # 統計餘數的數量
        cnt = [0] * k 
        for x in arr:
            cnt[x % k] += 1
        # 檢查是否能夠兩兩配對
        for i in range(1, (k + 1) // 2):
            if cnt[i] != cnt[k - i]:
                return False
        # 處理 k 為偶數的情況，k / 2 的餘數數量必須為偶數
        if k & 1 == 0 and cnt[k // 2] & 1:
            return False
        return cnt[k // 2] & 1
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5,10,6,7,8,9]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,6]\n7\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,6]\n10\n
# @lcpr case=end

#

