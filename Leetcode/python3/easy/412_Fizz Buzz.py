#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MAX_N = int(1e4 + 5)
ans = []
for i in range(1, MAX_N):
    flag1 = i % 3 == 0
    flag2 = i % 5 == 0
    if flag1 and flag2:
        ans.append('FizzBuzz')
    elif flag1:
        ans.append('Fizz')
    elif flag2:
        ans.append('Buzz')
    else:
        ans.append(str(i))

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return ans[:n]
# @lc code=end

