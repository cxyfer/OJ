# You are given a string word and an integer k.

# A substring s of word is complete if:

# Each character in s occurs exactly k times.
# The difference between two adjacent characters is at most 2. That is, for any two adjacent characters c1 and c2 in s, the absolute difference in their positions in the alphabet is at most 2.
# Return the number of complete substrings of word.

# A substring is a non-empty contiguous sequence of characters in a string.
from collections import Counter, defaultdict

class Solution:
    """
        分組循環 + 枚舉窗口大小 + 滑動窗口
        第二個限制「相鄰字母相差至多為 2」可以將 word 分成多個子串 s，每個字串 s 可以分別處理。
        對於每個字串 s ，枚舉出現的字母數量 m ，窗口大小為 k * m 的，此時可以用滑動窗口求出答案。
        Time: O(n * 26 * 26) 或 O(n * 26 * 1)
    """
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        ans = 0

        def f(s: str) -> int: # Sliding window
            res = 0
            for m in range(1, 27): # 枚舉出現的字母數量 m，且根據題目，每個字母需出現k次，故窗口大小為 k * m
                if k * m > len(s): # 窗口大小超過字串長度
                    break
                cnt = [0] * 26 # 窗口內每個字母出現的次數
                cnt_cnt = [0] * (k * m + 1) # 窗口內每個字母出現的次數的次數
                for right, ch in enumerate(s):
                    c_in = ord(ch) - ord('a')
                    cnt_cnt[cnt[c_in]] -= 1
                    cnt[c_in] += 1
                    cnt_cnt[cnt[c_in]] += 1
                    if right >= k * m - 1: # 窗口大小為 k * m，故窗口內的字母數量不足 k * m 時，不計算
                        left = right + 1 - k * m
                        c_out = ord(s[left]) - ord('a')
                        # 窗口內的字母數量都為 k 時，res + 1
                        # res += all(cnt[c] == 0 or cnt[c] == k for c in range(26)) # O(26)
                        if cnt_cnt[k] == m: # O(1)
                            res += 1
                        cnt_cnt[cnt[c_out]] -= 1
                        cnt[c_out] -= 1
                        cnt_cnt[cnt[c_out]] += 1
            return res
        
        # 分組循環
        j = 0 # j is the right pointer
        while j < n:
            i = j
            j += 1
            while j < n and abs(ord(word[j]) - ord(word[j - 1])) <= 2:
                j += 1
            # print(word[i:j])
            ans += f(word[i:j])
        return ans
sol = Solution()
print(sol.countCompleteSubstrings("igigee", 2)) # 3
print(sol.countCompleteSubstrings("aaabbbccc", 3)) # 6
print(sol.countCompleteSubstrings("gvgvvgv", 2)) # 1
print(sol.countCompleteSubstrings("hmfttfmhpttmpphmhthfpffphftfhthtmhthhfphfmmm", 1)) # 49