#
# @lc app=leetcode id=670 lang=python3
# @lcpr version=30204
#
# [670] Maximum Swap
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        n = len(s)
        idx = n - 1  # max idx
        left, right = 0, 0
        for i in range(n - 1, -1, -1):
            if s[i] > s[idx]:  # 更大的數
                idx = i
            elif s[i] < s[idx]:  # 可以交換的候選
                left, right = i, idx
            # 有多個相同的數可以交換，但取最右邊的，因此不用特別處理
        s[left], s[right] = s[right], s[left]
        return int(''.join(s))
    
class Solution2:
    def maximumSwap(self, num: int) -> int:
        lst = []
        while num > 0:
            lst.append(num % 10)
            num //= 10
        lst.reverse()
        n = len(lst)
        idx = n - 1  # max idx
        left, right = 0, 0
        for i in range(n - 1, -1, -1):
            if lst[i] > lst[idx]:
                idx = i
            elif lst[i] < lst[idx]:
                left, right = i, idx
        lst[left], lst[right] = lst[right], lst[left]
        ans = 0
        for x in lst:
            ans = ans * 10 + x
        return ans
    
class Solution(Solution2):
    pass
# @lc code=end



#
# @lcpr case=start
# 2736\n
# @lcpr case=end

# @lcpr case=start
# 9973\n
# @lcpr case=end

#

