#
# @lc app=leetcode id=567 lang=python3
# @lcpr version=30204
#
# [567] Permutation in String
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        cnt = Counter(s1)
        need = len(cnt)
        left = have = 0
        for right, ch in enumerate(s2):
            if ch in cnt:
                cnt[ch] -= 1
                if cnt[ch] == 0:
                    have += 1
            while right - left + 1 > len(s1):
                if s2[left] in cnt:
                    cnt[s2[left]] += 1
                    if cnt[s2[left]] == 1:
                        have -= 1
                left += 1
            if have == need:
                return True
        return False
    
class Solution2:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        cnt = Counter(s1) # 每個字元還需要的數量
        left = 0
        for right, ch in enumerate(s2):
            cnt[ch] -= 1
            while cnt[ch] < 0: # 這個字元的數量太多了
                cnt[s2[left]] += 1
                left += 1
            if right - left + 1 == len(s1): # 窗口大小等於 s1 的長度
                return True
        return False

class Solution(Solution2):
    pass
# @lc code=end



#
# @lcpr case=start
# "ab"\n"eidbaooo"\n
# @lcpr case=end

# @lcpr case=start
# "ab"\n"eidboaoo"\n
# @lcpr case=end

#

