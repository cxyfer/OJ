#
# @lc app=leetcode id=2938 lang=python3
# @lcpr version=30203
#
# [2938] Separate Black and White Balls
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        1. Two pointers，賽時寫法
            用雙指針 left, right 分別指向 s 的頭尾，然後循環，每次循環找到左邊第一個 1 和右邊第一個 0。
            如果 left < right，那麼我們需要將最右邊的 0 交換到最左邊的 1 的左邊，交換次數就是 right - left。
        2. 
        每次碰到 0 就貪心的將其往左交換直到它最終的位置，因為遇到當前的 0 時，前面的 0 都已經在最後的位置了，
        因此這個 0 左邊會是一連串的 1，所以只需要將這個 0 移動到 1 的左邊即可，需要移動的次數就是左邊的 1 的數量。
    """
    def minimumSteps(self, s: str) -> int:
        return self.solve1(s)
        # return self.solve2(s)
    def solve1(self, s: str) -> int:
        n = len(s)
        left, right = 0, n - 1
        ans = 0
        while left < right:
            while left < right and s[left] == '0': # find the first 1 from left
                left += 1
            while left < right and s[right] == '1': # find the first 0 from right
                right -= 1
            if left < right: # if left < right, we need to swap s[right] to position left
                ans += right - left # the number of swaps needed
                left += 1
                right -= 1
        return ans
    def solve2(self, s: str) -> int:
        ans = 0
        cnt = 0 # 每次遇到 0 時，左邊的 1 的數量
        for ch in s:
            if ch == '1':
                cnt += 1
            else:
                ans += cnt
        return ans
# @lc code=end



#
# @lcpr case=start
# "101"\n
# @lcpr case=end

# @lcpr case=start
# "100"\n
# @lcpr case=end

# @lcpr case=start
# "0111"\n
# @lcpr case=end

#

