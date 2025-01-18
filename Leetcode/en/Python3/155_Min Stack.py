# @algorithm @lc id=155 lang=python3 
# @title min-stack
"""
    同時保存當前值和當前最小值
"""
class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        if not self.st:
            self.st.append((val, val))
        else:
            self.st.append((val, min(val, self.st[-1][1]))) # 同時保存當前值和當前最小值

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]