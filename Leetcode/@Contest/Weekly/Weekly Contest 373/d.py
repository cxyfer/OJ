# You are given a string s and a positive integer k.

# Let vowels and consonants be the number of vowels and consonants in a string.

# A string is beautiful if:

# vowels == consonants.
# (vowels * consonants) % k == 0, in other terms the multiplication of vowels and consonants is divisible by k.
# Return the number of non-empty beautiful substrings in the given string s.

# A substring is a contiguous sequence of characters in a string.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

# Consonant letters in English are every letter except vowels.

from typing import List
from collections import Counter

class Solution:
    """
        k 是/不是 完全平方數的倍數
    """
    def beautifulSubstrings(self, s: str, k: int) -> int:
        
        n = len(s)
        k = 4 * k
        for p in range(int(k**0.5), 1, -1): # k <= 1000
            if k % (p ** 2) == 0:
                k //= p
                break
        # print(k)
            
        ans = 0
        vowels_set = set("aeiou")
        pre_sum = [0]
        for ch in s:
            x = 1 if ch in vowels_set else -1
            pre_sum.append(pre_sum[-1] + x)


        ans = 0
        cnt = Counter([(k - 1, 0)])
        for i in range(n): # 枚舉起點
            p = (i % k, pre_sum[i+1])
            ans += cnt[p]
            cnt[p] += 1
        return ans


sol = Solution()
print(sol.beautifulSubstrings("baeyh", 2)) # 2
print(sol.beautifulSubstrings("abba", 1)) # 3
print(sol.beautifulSubstrings("bcdf", 1)) # 0
print(sol.beautifulSubstrings("eeebjoxxujuaeoqibd", 8)) # 4