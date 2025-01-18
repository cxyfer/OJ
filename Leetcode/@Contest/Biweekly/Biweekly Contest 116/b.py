# You are given a 0-indexed binary string s having an even length.

# A string is beautiful if it's possible to partition it into one or more substrings such that:

# Each substring has an even length.
# Each substring contains only 1's or only 0's.
# You can change any character in s to 0 or 1.

# Return the minimum number of changes required to make the string s beautiful.

class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n//2):
            if s[2*i] != s[2*i+1]:
                ans += 1
        return ans
sol = Solution()
print(sol.minChanges("0100")) # 1
print(sol.minChanges("10")) # 1
print(sol.minChanges("1110")) # 1