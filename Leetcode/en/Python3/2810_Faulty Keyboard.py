# @algorithm @lc id=2886 lang=python3 
# @title faulty-keyboard


from en.Python3.mod.preImport import *
# @test("string")="rtsng"
# @test("poiinter")="ponter"
class Solution:
    def finalString(self, s: str) -> str:
        # return self.solve1(s)
        return self.solve2(s)
    def solve1(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            if s[i] == "i":
                ans = ans[::-1]
            else:
                ans += s[i]
        return ans
    """
        2. deque
    """
    def solve2(self, s: str) -> str:
        dq = deque()
        flag = False # 表示當前是否為反轉狀態
        for ch in s:
            if ch == "i":
                flag = not flag
            elif flag: # 若當前處於反轉狀態，則將字元插入到左邊
                dq.appendleft(ch)
            else: # 若當前處於正常狀態，則將字元插入到右邊
                dq.append(ch)
        return "".join(dq if not flag else reversed(dq)) 