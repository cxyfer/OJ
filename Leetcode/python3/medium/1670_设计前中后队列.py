#
# @lc app=leetcode.cn id=1670 lang=python3
#
# [1670] 设计前中后队列
#
from preImport import *
# @lc code=start
"""
    用兩個deque實現
"""
class FrontMiddleBackQueue:
    __slots__ = ["left", "right"]

    def __init__(self):
        self.left = deque()
        self.right = deque()

    # 確保 0 <= len(right) - len(left) <= 1
    # 這樣才能在正中間插入刪除元素
    def balance(self):
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())
        elif len(self.right) > len(self.left) + 1:
            self.left.append(self.right.popleft())

    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        self.balance()

    def pushMiddle(self, val: int) -> None:
        if len(self.left) < len(self.right):
            self.left.append(val)
        else:
            self.right.appendleft(val)

    def pushBack(self, val: int) -> None:
        self.right.append(val)
        self.balance()

    def popFront(self) -> int:
        if not self.right:  # empty
            return -1
        val = self.left.popleft() if self.left else self.right.popleft()
        self.balance()
        return val

    def popMiddle(self) -> int:
        if not self.right:
            return -1
        if len(self.left) == len(self.right):
            return self.left.pop()
        return self.right.popleft()
    def popBack(self) -> int:
        if not self.right:  # empty
            return -1
        val = self.right.pop()
        self.balance()
        return val

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
# @lc code=end

