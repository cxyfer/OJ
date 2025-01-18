#
# @lc app=leetcode.cn id=2591 lang=python3
#
# [2591] 将钱分给最多的儿童
#

# @lc code=start
class Solution:
    def distMoney(self, money: int, children: int) -> int:
        # 初步分配，讓盡量多的人分到 8 元
        money -= children # 先分給每人1元
        if money < 0: # 錢不夠分
            return -1
        ans = min(money // 7, children) # 有多少人拿1+7元
        # 初步分配完後，剩下的錢必少於7元，剩下的錢要分給沒有拿到8元的人
        remainder = money - ans * 7 # 剩下的錢
        children -= ans # 剩下的人數
        # 還有錢，但是沒有人可以分，讓一個人多分，ans-1
        # 或者只有一個人，但剩下3元，不滿足題意的分配方式，同樣要讓一個人多分，ans-1
        if children == 0 and remainder or children == 1 and remainder == 3:
            ans -= 1
        return ans
# @lc code=end
sol = Solution()
print(sol.distMoney(23,2))
print(sol.distMoney(20,3))
print(sol.distMoney(16,2))

