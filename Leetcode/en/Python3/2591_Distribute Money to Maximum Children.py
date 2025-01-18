# @algorithm @lc id=2663 lang=python3 
# @title distribute-money-to-maximum-children


from en.Python3.mod.preImport import *
# @test(20,3)=1
# @test(16,2)=2
class Solution:
    """
        Greedy
        1. 初步分配，讓盡量多的人分到 8 元
        2. 初步分配完後
            2a. 剩下的錢少於7元，剩下的錢要分給沒有拿到8元的人，並確保沒有人拿到4元
                - 只有當剩下1人且剩下3元時，才不滿足題意的分配方式，讓一個原本拿到8元的人多分，ans-1
            2b. 全部人都拿到8元，但是還有錢，讓一個人多分剩下的錢，ans-1
    """
    def distMoney(self, money: int, children: int) -> int:
        # 1. 初步分配，讓盡量多的人分到 8 元
        money -= children # 先分給每人1元
        if money < 0:
            return -1
        ans = min(money // 7, children) # 有多少人拿1+7元

        # 2. 初步分配完後
        remainder = money - ans * 7 # 剩下的錢
        children -= ans # 剩下的人數
        if (children == 0 and remainder) or (children == 1 and remainder == 3): # 2b or 2a
            ans -= 1
        return ans