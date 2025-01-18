"""
    模板來自 https://leetcode.cn/circle/discuss/SJFwQI/
"""

class Manacher:
    def __init__(self, s) -> None:
        self.s = s
        if isinstance(s, str):
            self.t = '#'.join("^" + s + "$")
        elif isinstance(s, list):
            self.t = '#'.join(['^'] + s + ['$'])
        else:
            raise ValueError("s must be a string or a list")
        
        self.halfLen = [0] * (len(self.t) - 2)
        self.halfLen[1] = 1
        boxM = boxR = 0
        self.max_i = 0 # 最長回文子字串的中心位置
        for i in range(2, len(self.halfLen)):
            hl = 1
            if i < boxR:
                hl = min(self.halfLen[boxM * 2 - i], boxR - i)
            while self.t[i - hl] == self.t[i + hl]:
                hl += 1
                boxM, boxR = i, i + hl
            self.halfLen[i] = hl
            if hl > self.halfLen[self.max_i]:
                self.max_i = i

    # 判斷 s[l:r] 是否為回文字串
    def isPalindrome(self, l: int, r: int) -> bool:
        return self.halfLen[l + r + 1] > r - l
    
    # 獲取最長回文子字串的長度
    def getMaxPalindromeLength(self) -> int:
        return self.halfLen[self.max_i] - 1
    
    # 獲取最長回文子字串
    def getMaxPalindrome(self) -> str:
        hl = self.halfLen[self.max_i]
        return self.s[(self.max_i - hl) // 2:(self.max_i + hl) // 2 - 1]
    
