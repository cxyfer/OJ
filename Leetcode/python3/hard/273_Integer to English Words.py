#
# @lc app=leetcode id=273 lang=python3
# @lcpr version=30204
#
# [273] Integer to English Words
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def numberToWords(self, num: int) -> str:
        mp = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four',
              5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
              10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
              15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen',
              20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty',
              70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}

        def convert(num):
            if num >= 10 ** 9:
                base = 10 ** 9
                unit = 'Billion'
            elif num >= 10 ** 6:
                base = 10 ** 6
                unit = 'Million'
            elif num >= 10 ** 3:
                base = 10 ** 3
                unit = 'Thousand'
            elif num >= 10 ** 2:
                base = 10 ** 2
                unit = 'Hundred'
            else:
                return mp[num] if num in mp else mp[num // 10 * 10] + " " + mp[num % 10]
            
            r = num % base
            if r == 0:
                return convert(num // base) + " " + unit 
            else:
                return convert(num // base) + " " + unit + " " + convert(r)
                
        return convert(num)
# @lc code=end



#
# @lcpr case=start
# 123\n
# @lcpr case=end

# @lcpr case=start
# 12345\n
# @lcpr case=end

# @lcpr case=start
# 1234567\n
# @lcpr case=end

#

