#
# @lc app=leetcode id=2053 lang=python3
# @lcpr version=30204
#
# [2053] Kth Distinct String in an Array
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cnt = Counter(arr)
        for s in arr:
            if cnt[s] == 1:
                k -= 1
                if k == 0:
                    return s
        return ''
# @lc code=end



#
# @lcpr case=start
# ["d","b","c","b","c","a"]\n2\n
# @lcpr case=end

# @lcpr case=start
# ["aaa","aa","a"]\n1\n
# @lcpr case=end

# @lcpr case=start
# ["a","b","a"]\n3\n
# @lcpr case=end

#

