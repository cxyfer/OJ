class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        left, right = 0, n - 1
        ans = 0
        while left < right:
            while left < n and s[left] == '0':
                left += 1
            while right >= 0 and s[right] == '1':
                right -= 1
            if left < right:
                ans += right - left
            left += 1
            right -= 1
        return ans

sol = Solution()
print(sol.minimumSteps("101")) # 1
print(sol.minimumSteps("100")) # 2
print(sol.minimumSteps("0000000000001111111111111111")) # 0

print(sol.minimumSteps("0100101")) # 4
print(sol.minimumSteps("010010000")) 