#
# @lc app=leetcode id=2264 lang=python3
# @lcpr version=30204
#
# [2264] Largest 3-Same-Digit Number in String
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. Sliding window
窗口大小固定為3，每次移動一格，並更新窗口內的數字出現次數。
- 若檢查所有數字的出現次數，則時間複雜度為 $O(10)$
- 若同時統計出現次數的出現次數，則不用逐個字檢查，時間複雜度為 $O(1)$

2. 分組循環
檢查每段長度是否 >= 3 即可
"""
# @lc code=start
class Solution1:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""
        cnt = [0] * 10 # 每個數字出現的次數
        cntcnt = [0] * (3 + 1) # 出現次數的出現次數為 0, 1, 2, 3
        for right, ch in enumerate(num):
            x = ord(ch) - ord('0') # 入窗口
            cntcnt[cnt[x]] -= 1
            cnt[x] += 1
            cntcnt[cnt[x]] += 1

            left = right - 3 + 1
            if left >= 0: # 窗口大小固定為 3
                if cntcnt[3] > 0: # 窗口內有出現 3 次的數字，則更新答案
                    ans = num[left:right+1] if num[left:right+1] > ans else ans
                y = ord(num[left]) - ord('0') # 出窗口
                cntcnt[cnt[y]] -= 1
                cnt[y] -= 1
                cntcnt[cnt[y]] += 1
        return ans
    
class Solution2:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""
        for c, l in groupby(num):
            if len(list(l)) >= 3:
                ans = max(ans, c * 3)
        return ans

# Solution = Solution1
Solution = Solution2
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

