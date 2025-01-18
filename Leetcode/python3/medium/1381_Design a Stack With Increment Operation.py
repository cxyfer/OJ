#
# @lc app=leetcode id=1381 lang=python3
# @lcpr version=30204
#
# [1381] Design a Stack With Increment Operation
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class CustomStack:

    def __init__(self, maxSize: int):
        self.top = -1
        self.st = [0] * maxSize
        self.lazy = [0] * maxSize # lazy tag

    def push(self, x: int) -> None:
        if self.top + 1 == len(self.st):
            return
        self.top += 1
        self.st[self.top] = x

    def pop(self) -> int:
        if self.top == -1:
            return -1
        res = self.st[self.top] + self.lazy[self.top]
        if self.top != 0: # 不是最底層的話，把 lazy tag 往下傳
            self.lazy[self.top - 1] += self.lazy[self.top]
        self.lazy[self.top] = 0 # 清掉 lazy tag
        self.top -= 1
        return res
        
    def increment(self, k: int, val: int) -> None:
        idx = min(k - 1, self.top) # 最多只會影響到下標為 top 的元素
        if idx >= 0:
            self.lazy[idx] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
# @lc code=end



