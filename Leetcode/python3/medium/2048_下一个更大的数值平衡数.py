2#
# @lc app=leetcode.cn id=2048 lang=python3
#
# [2048] 下一个更大的数值平衡数
#
from preImport import *
# @lc code=start
class Solution:
    """
        http://gdst.dev/posts/LC_23Dec/#2023-12-09
    """
    def nextBeautifulNumber(self, n: int) -> int:
        l, tmp = 0, n
        while tmp > 0:
            l += 1
            tmp //= 10
        ans = []
        path1, path2 = [], []
        def perm(digits: dict): # 考慮重複物排列
            if all(v == 0 for v in digits.values()):
                ans.append(int(''.join(map(str, path2))))
                return
            for k, v in digits.items():
                if v <= 0:
                    continue
                path2.append(k)
                digits[k] -= 1
                perm(digits)
                digits[k] += 1
                path2.pop()

        def backtrack(d: int): # 符合題目的數字
            if sum(path1) > d: # 超過要求的位數
                return
            if sum(path1) == d: # 符合要求的位數
                cnt = {i:i for i in path1}
                perm(cnt)
                return
            last = path1[-1] if path1 else 0
            for i in range(last+1, 10):
                path1.append(i)
                backtrack(d)
                path1.pop()
        
        if l > 0:
            backtrack(l)
        backtrack(l+1)

        ans.sort()
        return ans[bisect_right(ans, n)]
# @lc code=end
sol = Solution()
print(sol.nextBeautifulNumber(0)) # 1
print(sol.nextBeautifulNumber(1)) # 22
print(sol.nextBeautifulNumber(1000)) # 1333
print(sol.nextBeautifulNumber(3000)) # 3133

print(sol.nextBeautifulNumber(300000)) 
