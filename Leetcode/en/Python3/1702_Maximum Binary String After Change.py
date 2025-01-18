# @algorithm @lc id=1804 lang=python3 
# @title maximum-binary-string-after-change


from en.Python3.mod.preImport import *
# @test("000110")="111011"
# @test("01")="01"
class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        # return self.solve1(binary)
        return self.solve2(binary)
    """
        1. Greedy 找規律模擬

        010 -> 001 -> 101
        000010 -> 111101
        011101 -> 101111

        遇到 0 的時候，找下一個出現的 0 的位置，
        將第一個 0 變為 1 ，且將其下一個位置變為 0，第二個 0 變為 1
    """
    def solve1(self, binary: str) -> str:
        n = len(binary)
        s = list(binary)
        j = 0
        for i in range(n):
            if s[i] == '0': # 第一個 0
                if j <= i:
                    j = i + 1
                while j < n and s[j] == '1': # 找第二個 0
                    j += 1
                if j < n: # 找到第二個 0
                    s[j] = '1'
                    s[i] = '1'
                    s[i + 1] = '0'
        return ''.join(s)
    """
        2. Greedy 直接構建
        觀察到，如果原字串有 0 的話，則不管有多少個 0 ，最後一定會只有一個 0
        若原字串只有一個 0 ，則出現在第一個 0 的位置，若再每多一個 0 ，則 0 的位置會往後移動一位
    """
    def solve2(self, binary: str) -> str:
        n = len(binary)
        idx = binary.find("0") # 第一個 0 的位置
        if idx < 0: # 沒有 0，直接返回
            return binary
        cnt0 = binary.count('0') # 0 的個數
        ans = ['1'] * n
        ans[idx + cnt0 - 1] = '0' # 往後移動 cnt0 - 1 位
        return ''.join(ans)