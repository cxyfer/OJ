# 7020. Count Symmetric Integers

# You are given two positive integers low and high.

# An integer x consisting of 2 * n digits is symmetric if the sum of the first n digits of x is equal to the sum of the last n digits of x. Numbers with an odd number of digits are never symmetric.

# Return the number of symmetric integers in the range [low, high].

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for i in range(low, high+1):
            if len(str(i)) % 2 == 1:
                continue
            lst = list(str(i))
            if sum(map(int, lst[:len(lst)//2])) == sum(map(int, lst[len(lst)//2:])):
                ans += 1
        return ans

sol = Solution()
print(sol.countSymmetricIntegers(1, 100))
print(sol.countSymmetricIntegers(1200, 1230))