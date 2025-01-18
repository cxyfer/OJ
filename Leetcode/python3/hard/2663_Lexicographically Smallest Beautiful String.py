#
# @lc app=leetcode id=2663 lang=python3
# @lcpr version=30204
#
# [2663] Lexicographically Smallest Beautiful String
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    想成 k 進位制，每次進位時，檢查是否有回文字串，若有則繼續進位。
    若一個字串 s 不是回文字串，則其任意長度 > 1 的子字串都不是回文字串。
    => 只需要考慮長度為 2 和 3 的子字串是否為回文字串即可。
    
    利用給定的 s 為非回文字串的性質，來確保未被修改過的部分與其前面的字元都不會形成回文字串。
"""
class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        toInt = lambda ch: ord(ch) - ord('a')
        toChar = lambda x: chr(x + ord('a'))

        n = len(s)
        lst = list(map(toInt, s))
        i = n - 1 # 從最後一位開始
        lst[i] += 1 # 先加一

        while i < n:
            # Case 1: 需要進位
            if lst[i] == k: 
                if i == 0: # 無法進位
                    return ""
                lst[i] = 0
                lst[i - 1] += 1
                i -= 1
            # Case 2: 如果 lst[i] 和左側字元相同，或者和左側的左側字元相同，則會形成回文字串，需要繼續增加 lst[i]
            elif i and lst[i] == lst[i - 1] or i > 1 and lst[i] == lst[i - 2]:
                lst[i] += 1
            # Case 3: 若為其他情況，則根據約束條件，前面已經沒有回文字串了，重新往後檢查是否有回文字串
            else: 
                i += 1

        return ''.join(map(toChar, lst))
# @lc code=end



#
# @lcpr case=start
# "abcz"\n26\n
# @lcpr case=end

# @lcpr case=start
# "dc"\n4\n
# @lcpr case=end

#

