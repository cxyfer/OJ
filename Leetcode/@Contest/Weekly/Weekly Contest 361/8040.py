# 8040. Minimum Operations to Make a Special Number

# You are given a 0-indexed string num representing a non-negative integer.

# In one operation, you can pick any digit of num and delete it. Note that if you delete all the digits of num, num becomes 0.

# Return the minimum number of operations required to make num special.

# An integer x is considered special if it is divisible by 25.

class Solution:
    def minimumOperations(self, num: str) -> int:
        # 讓最後兩位是25, 50, 75, 00的最小操作次數
        n = len(num)
        lst = list(num)
        if int(num[n-2:]) % 25 == 0: # 25, 50, 75, 00
            return 0
        if n == 2:
            if num.count('0') == 1:
                return 1
            else:
                return 2
        if n == 1:
            if int(num) % 25 == 0:
                return 0
            else:
                return 1
        # 分別考慮 25, 50, 75, 00
        ans = float('inf')
        for target in ["25", "50", "75", "00"]:
            right = n-1
            count = 0
            for ch in reversed(target):
                while right >= 0 and lst[right] != ch:
                    count += 1
                    right -= 1
                right -= 1
            print(target, right, count)
            if right >= -1:
                ans = min(ans, count)
        if ans != float('inf') :
            return ans
        else:
            if num.count('0') == 1:
                return n-1
            else:
                return n




sol = Solution()
# print(sol.minimumOperations("2245047")) # 2
# print(sol.minimumOperations("2908305")) # 3
# print(sol.minimumOperations("10")) # 1
# print(sol.minimumOperations("1")) # 1
# print(sol.minimumOperations("528033")) # 4
print(sol.minimumOperations("820366")) # 5
