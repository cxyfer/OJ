#
# @lc app=leetcode id=3295 lang=python3
# @lcpr version=30204
#
# [3295] Report Spam Message
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        bans = set(bannedWords)
        cnt = 0
        for word in message:
            if word in bans:
                cnt += 1
                if cnt >= 2:
                    return True
        return False
# @lc code=end



#
# @lcpr case=start
# ["hello","world","leetcode"]\n["world","hello"]\n
# @lcpr case=end

# @lcpr case=start
# ["hello","programming","fun"]\n["world","programming","leetcode"]\n
# @lcpr case=end

#

