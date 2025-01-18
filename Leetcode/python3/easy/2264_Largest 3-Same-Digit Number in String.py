#
# @lc app=leetcode id=2264 lang=python3
# @lcpr version=30204
#
# [2264] Largest 3-Same-Digit Number in String
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    Sliding window
    窗口大小固定為3，每次移動一格，並更新窗口內的數字出現次數。
    - 若檢查所有數字的出現次數，則時間複雜度為 $O(10)$
    - 若同時統計出現次數的出現次數，則不用逐個字檢查，時間複雜度為 $O(1)$
"""
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        ans = ""

        cnt = [0] * 10 # 每個數字出現的次數
        cntcnt = [0] * (3 + 1) # 出現次數的出現次數為 0, 1, 2, 3

        for right in range(n):
            ch_in = ord(num[right]) - ord('0') # 入窗口
            cntcnt[cnt[ch_in]] -= 1
            cnt[ch_in] += 1
            cntcnt[cnt[ch_in]] += 1

            left = right - 3 + 1
            if left >= 0: # 窗口大小固定為3
                if cntcnt[3] > 0: # 窗口內有出現3次的數字，則更新答案
                    ans = num[left:right+1] if num[left:right+1] > ans else ans
                    
                ch_out = ord(num[left]) - ord('0') # 出窗口
                cntcnt[cnt[ch_out]] -= 1
                cnt[ch_out] -= 1
                cntcnt[cnt[ch_out]] += 1
        return ans
# @lc code=end



#
# @lcpr case=start
# "6777133339"\n
# @lcpr case=end

# @lcpr case=start
# "2300019"\n
# @lcpr case=end

# @lcpr case=start
# "42352338"\n
# @lcpr case=end

#

