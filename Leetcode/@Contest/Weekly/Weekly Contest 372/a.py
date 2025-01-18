class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        x, y, z = len(s1), len(s2), len(s3)
        n = min(x, y, z)
        # 枚舉剩下的字串
        ans = 0
        for i in range(n):
            if s1[i] == s2[i] and s2[i] == s3[i]:
                ans += 1
            else:
                break
        return ans if ans != 0 else -1

sol = Solution()
print(sol.findMinimumOperations("abc", "abb", "ab")) # 2
print(sol.findMinimumOperations("dac", "bac", "cac")) # -1