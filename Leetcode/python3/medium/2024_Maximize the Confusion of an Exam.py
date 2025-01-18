#
# @lc app=leetcode id=2024 lang=python3
# @lcpr version=30204
#
# [2024] Maximize the Confusion of an Exam
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        Sliding window
        Similar to 1004. Max Consecutive Ones III
        轉換成找一個最長的子字串，使得子字串中 T/F 的個數不超過k個
    """
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        def helper(ch: str):
            cnt = 0 # 窗口中 ch 的個數
            left = 0 # 左端點
            res = 0 # 窗口的最大長度
            for right in range(n): # 枚舉右端點，入窗口
                if answerKey[right] == ch:
                    cnt += 1
                while cnt > k: # 不滿足條件，開始縮小窗口
                    if answerKey[left] == ch:
                        cnt -= 1
                    left += 1
                res = max(res, right - left + 1) # 更新答案
            return res
        return max(helper('T'), helper('F'))
# @lc code=end

#
# @lcpr case=start
# "TTFF"\n2\n
# @lcpr case=end

# @lcpr case=start
# "TFFT"\n1\n
# @lcpr case=end

# @lcpr case=start
# "TTFTTFTT"\n1\n
# @lcpr case=end

#

