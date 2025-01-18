#
# @lc app=leetcode id=2168 lang=python3
# @lcpr version=30204
#
# [2168] Unique Substrings With Equal Digit Frequency
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. Brute Force: O(n^2*(D+n))
2. Optimized Brute Force: O(n^3)
3. Trie: O(n^2*D)
4. Rolling Hash: O(n^2)
"""
# @lc code=start
class Solution1:
    def equalDigitFrequency(self, s: str) -> int:
        n = len(s)
        st = set()
        for i in range(n):
            cnt = [0] * 10
            for j in range(i, n):
                d = ord(s[j]) - ord('0')
                cnt[d] += 1
                mx = max(cnt)
                if all(x == 0 or x == mx for x in cnt):  # O(D)
                    st.add(s[i:j+1])  # O(n)
        return len(st)

class Solution2:
    def equalDigitFrequency(self, s: str) -> int:
        n = len(s)
        st = set()
        for i in range(n):
            cnt = [0] * 10
            mx = sz = 0
            for j in range(i, n):
                d = ord(s[j]) - ord('0')
                cnt[d] += 1
                if cnt[d] == 1:
                    sz += 1
                mx = max(mx, cnt[d])
                if mx * sz == j - i + 1:  # O(1)
                    st.add(s[i:j+1])  # O(n)
        return len(st)

class TrieNode:
    def __init__(self):
        self.child = [None] * 10
        self.isEnd = False

class Solution3:
    def equalDigitFrequency(self, s: str) -> int:
        n = len(s)
        ans = 0
        root = TrieNode()
        for i in range(n):
            cnt = [0] * 10
            mx = sz = 0
            node = root
            for j in range(i, n):
                d = ord(s[j]) - ord('0')
                if node.child[d] is None:
                    node.child[d] = TrieNode()
                node = node.child[d]

                cnt[d] += 1
                if cnt[d] == 1:
                    sz += 1
                mx = max(mx, cnt[d])

                if not node.isEnd:
                    if mx * sz == j - i + 1:
                        ans += 1
                    node.isEnd = True
        return ans
    
class Solution4:
    def equalDigitFrequency(self, s: str) -> int:
        n = len(s)
        MOD = 1070777777
        BASE = randint(int(1e8), int(1e9))
        st = set()
        for i in range(n):
            cnt = [0] * 10
            mx = sz = 0
            hs = 0
            for j in range(i, n):
                d = ord(s[j]) - ord('0')
                hs = (hs * BASE + ord(s[j])) % MOD  # 不能直接用 d，不然 "0" 和空字串 "" 雜湊值是相同的
                cnt[d] += 1
                if cnt[d] == 1:
                    sz += 1
                mx = max(mx, cnt[d])
                if mx * sz == j - i + 1:
                    st.add(hs)
        return len(st)

class Solution(Solution4):
    pass

# @lc code=end

sol = Solution()
print(sol.equalDigitFrequency("1212"))  # 5
print(sol.equalDigitFrequency("12321"))  # 9
print(sol.equalDigitFrequency("012345"))  # 21
#
# @lcpr case=start
# "1212"\n
# @lcpr case=end

# @lcpr case=start
# "12321"\n
# @lcpr case=end

#

