#
# @lc app=leetcode id=387 lang=python3
# @lcpr version=30201
#
# [387] First Unique Character in a String
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        1. Hash Table
            使用 Counter 來計算每個字母出現的次數，再遍歷一次 s 找到第一個只出現一次的字母
            - Time: O(n)
            - Space: O(\Sigma) = O(26) = O(1)
        2. Hash Table
            類似 1. ，但是改成保存每個字母的位置，若重複出現則設為 -1。第二次遍歷時只需要遍歷 Hash Table 即可
            - Time: O(n)
            - Space: O(\Sigma) = O(26) = O(1)
        3. Hash Table + Queue
            類似 2. ，但使用 Queue 來維護第一個出現的唯一字母，一次遍歷
    """
    def firstUniqChar(self, s: str) -> int:
        # return self.solve1(s)
        # return self.solve2(s)
        return self.solve3(s)
    def solve1(self, s: str) -> int:
        cnt = Counter(s)
        for i, ch in enumerate(s):
            if cnt[ch] == 1:
                return i
        return -1
    def solve2(self, s: str) -> int:
        pos = dict() # 保存每個字母的位置
        for i, ch in enumerate(s):
            pos[ch] = i if ch not in pos else -1
        ans = float('inf')
        for p in pos.values():
            if p != -1 and p < ans:
                ans = p
        return ans if ans != float('inf') else -1
    def solve3(self, s: str) -> int:
        pos = dict()
        q = deque()
        for i, ch in enumerate(s):
            if ch not in pos:
                pos[ch] = i
                q.append(ch)
            else:
                pos[ch] = -1
                while q and pos[q[0]] == -1: # 只需要確保 q[0] 是唯一的即可
                    q.popleft()
        return pos[q[0]] if q else -1
# @lc code=end



#
# @lcpr case=start
# "leetcode"\n
# @lcpr case=end

# @lcpr case=start
# "loveleetcode"\n
# @lcpr case=end

# @lcpr case=start
# "aabb"\n
# @lcpr case=end

#

