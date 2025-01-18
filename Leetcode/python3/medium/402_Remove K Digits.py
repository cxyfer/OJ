#
# @lc app=leetcode id=402 lang=python3
# @lcpr version=30201
#
# [402] Remove K Digits
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        Greedy + Stack
        貪心思路是讓前面的數字盡量小，所以當遇到比前面的數字還小的數字時，就將前面的數字刪除
        將問題轉換成保留 n - k 個數字
    """
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        left = n - k # 將問題轉換成保留 n - k 個數字
        st = []
        for d in num:
            while k and st and st[-1] > d: # 還能刪且遇到更小的數字
                st.pop()
                k -= 1
            st.append(d)
        ans = ''.join(st[:left]).lstrip("0") # 有可能會一直無法刪，此時保留前 left 個數字即可
        return ans if ans else "0"
# @lc code=end



#
# @lcpr case=start
# "1432219"\n3\n
# @lcpr case=end

# @lcpr case=start
# "10200"\n1\n
# @lcpr case=end

# @lcpr case=start
# "10"\n2\n
# @lcpr case=end

#

