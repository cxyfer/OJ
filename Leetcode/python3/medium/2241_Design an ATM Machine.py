#
# @lc app=leetcode id=2241 lang=python3
# @lcpr version=30204
#
# [2241] Design an ATM Machine
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
DENOMINATIONS = [20, 50, 100, 200, 500]
KINDS = len(DENOMINATIONS)
class ATM:

    def __init__(self):
        self.cnt = [0] * KINDS

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, v in enumerate(banknotesCount):
            self.cnt[i] += v

    def withdraw(self, amount: int) -> List[int]:
        ans = [0] * KINDS
        for i in range(KINDS-1, -1, -1):
            v = DENOMINATIONS[i]
            ans[i] = min(self.cnt[i], amount // v)
            amount -= ans[i] * v
        if amount != 0:
            return [-1]
        for i in range(KINDS):
            self.cnt[i] -= ans[i]
        return ans

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
# @lc code=end



