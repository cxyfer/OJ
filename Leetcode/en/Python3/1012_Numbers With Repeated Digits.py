# @algorithm @lc id=1057 lang=python3 
# @title numbers-with-repeated-digits


from en.Python3.mod.preImport import *
# @test(20)=1
# @test(100)=10
# @test(1000)=262
class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
                # Digit DP
        # Digit DP Template: https://www.bilibili.com/video/BV1rS4y1s721/
        # Similar to 902. Numbers At Most N Given Digit Set
        # Similar to 2376. 统计特殊整数
        # 所問的數字是 0~n 中的特殊數字，即每個digit都是0~9中的一個，且沒有重複的digit

        s = str(n)

        # cal(i, mask, is_limit, is_num) 表示当前已经填了前 i 位，当前的数字为 mask，之前的数字是否和 n 相等为 is_limit，之前是否已经填了一个合法数字为 is_num
        # mask 為二進位表示的集合，例如集合 {0,2,3} 對應的二進位表示為 1101，即 mask = 13
        #   如果 d 在 mask 中，則 mask >> d & 1 == 1
        #   把 d 加入 mask 中，則 mask = mask | (1 << d)
        # is_limit 表示之前的digit都和n一樣，所以這一位最大只能填s[i]
        # is_num 表示之前已經填了一個合法數字，因為不能有前導0，如果為False，則可以跳過當前digit或從1開始填，如果為True，則可以從0開始填

        @cache # memoize
        def cal(i: int, mask: int, is_limit: bool, is_num: bool) -> int:
            if i == len(s): # 填完所有位數，若此數字合法(is_num)，則返回1，否則返回0
                return int(is_num)
            res = 0 # 當前位數下，符合條件的特殊數字數量，初始為0
            if not is_num:  # 當還沒填合法數字時，可跳過當前digit
                res = cal(i + 1, mask, False, False)
            lower = 0 if is_num else 1  # is_num
            upper = int(s[i]) if is_limit else 9  # is_limit
            for d in range(lower, upper + 1):  # 遍歷當前digit
                if (mask >> d & 1) == 0:  # 若 d 不在 mask 中，即 d 沒有填過
                    res += cal(i + 1, mask | (1 << d), is_limit and d == upper, True) # 將此位填入 d，並更新 mask
            return res
        return n - cal(0, 0, True, False)