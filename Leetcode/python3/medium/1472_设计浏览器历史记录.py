#
# @lc app=leetcode.cn id=1472 lang=python3
#
# [1472] 设计浏览器历史记录
#
from preImport import *
# @lc code=start
class BrowserHistory1: # 1. Two Stacks

    def __init__(self, homepage: str):
        self.st1 = [homepage] # history
        self.st2 = [] # forward

    def visit(self, url: str) -> None:
        self.st1.append(url)
        self.st2 = [] # clear forward

    def back(self, steps: int) -> str:
        while steps > 0 and len(self.st1) > 1:
            self.st2.append(self.st1.pop())
            steps -= 1
        return self.st1[-1]

    def forward(self, steps: int) -> str:
        while steps > 0 and self.st2:
            self.st1.append(self.st2.pop())
            steps -= 1
        return self.st1[-1]

class BrowserHistory2: # 2. Dynamic Array

    def __init__(self, homepage: str):
        self.pages = [homepage]
        self.idx = 0

    def visit(self, url: str) -> None:
        del self.pages[self.idx+1:]
        self.pages.append(url)
        self.idx += 1

    def back(self, steps: int) -> str:
        self.idx = max(self.idx - steps, 0)
        return self.pages[self.idx]

    def forward(self, steps: int) -> str:
        self.idx = min(self.idx + steps, len(self.pages) - 1)
        return self.pages[self.idx]
# class BrowserHistory(BrowserHistory1):
class BrowserHistory(BrowserHistory2):
    pass
# @lc code=end

