#
# @lc app=leetcode id=2288 lang=python3
# @lcpr version=30203
#
# [2288] Apply Discount to Prices
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        d = (100 - discount) / 100
        words = sentence.split()
        for i, s in enumerate(words):
            if s[0] == '$' and s[1:].isdigit():
                price = int(s[1:]) * d
                words[i] = "$" + f"{price:.2f}"
        return " ".join(words)
# @lc code=end



#
# @lcpr case=start
# "there are $1 $2 and 5$ candies in the shop"\n50\n
# @lcpr case=end

# @lcpr case=start
# "1 2 $3 4 $5 $6 7 8$ $9 $10$"\n100\n
# @lcpr case=end

#

