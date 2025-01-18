#
# @lc app=leetcode id=1542 lang=python3
# @lcpr version=30202
#
# [1542] Find Longest Awesome Substring
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """ 前綴異或和
        由於可以重新排列，因此我們只要關心子字串的長度是否為奇數，以及每個字元的出現次數的奇偶性即可。
        1. 若子字串長度為偶數，則所有字元的出現次數都應為偶數。
        2. 若子字串長度為奇數，則除了一個字元的出現次數為奇數外，其他字元的出現次數都應為偶數。
        令 cur << i 為 1 表示第 i 個字元出現奇數次，0 表示出現偶數次。

        對於情況 1，顯然每個狀態與自己就構成了一個符合條件的子字串；
        對於情況 2，若存在一個狀態與自己 XOR 後只有一個 1 的狀態，則兩者間的子字串就滿足條件，因此可以反轉當前狀態每一位，檢查是否存在這樣的狀態。
        因此只需保存每個狀態「最早」出現的位置，當再次出現時計算兩者間的距離即可。
    """
    def longestAwesome(self, s: str) -> int:
        last = {0: -1} # 保存每個狀態「最早」出現的位置。空字串的狀態為所有字元出現次數都為偶數，即 0，位置可以視為 -1
        ans, cur = 0, 0 # ans: 最長超棒子字串的長度, cur: 當前狀態(前綴異或和)
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('0') # s 僅由數字組成
            cur ^= 1 << idx # 更新當前狀態
            if cur not in last:
                last[cur] = i # 這次迴圈不會用到這個狀態，所以可以直接更新
            else:
                ans = max(ans, i - last[cur])
            for j in range(10): # 檢查是否存在一個狀態與自己 XOR 後只有一個 1 的狀態
                if cur ^ (1 << j) in last:
                    ans = max(ans, i - last[cur ^ (1 << j)])
        return ans 
# @lc code=end



#
# @lcpr case=start
# "3242415"\n
# @lcpr case=end

# @lcpr case=start
# "12345678"\n
# @lcpr case=end

# @lcpr case=start
# "213123"\n
# @lcpr case=end

#