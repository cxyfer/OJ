# You are given a string s and a positive integer k.

# Let vowels and consonants be the number of vowels and consonants in a string.

# A string is beautiful if:

# vowels == consonants.
# (vowels * consonants) % k == 0, in other terms the multiplication of vowels and consonants is divisible by k.
# Return the number of non-empty beautiful substrings in the given string s.

# A substring is a contiguous sequence of characters in a string.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

# Consonant letters in English are every letter except vowels.

class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        vowels = consonants = 0
        pre_v = [0] * (n+1)  
        pre_c = [0] * (n+1)
        for i in range(n):
            if s[i] in "aeiou":
                vowels += 1
            else:
                consonants += 1
            pre_v[i+1] = vowels
            pre_c[i+1] = consonants
        # print(pre_v)
        # print(pre_c)
        for i in range(n): # 枚舉起點
            for j in range(i + 1, n+1): # 枚舉終點
                vowels = pre_v[j] - pre_v[i]
                consonants = pre_c[j] - pre_c[i]
                # print(i, j, s[i:j] ,vowels, consonants)
                if vowels == consonants and vowels * consonants % k == 0:
                    ans += 1
        return ans




sol = Solution()

print(sol.beautifulSubstrings("baeyh", 2)) # 2
print(sol.beautifulSubstrings("abba", 1)) # 3
print(sol.beautifulSubstrings("bcdf", 1)) # 0