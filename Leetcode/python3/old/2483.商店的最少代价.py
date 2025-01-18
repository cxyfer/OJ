#
# @lc app=leetcode.cn id=2483 lang=python3
#
# [2483] 商店的最少代价
#

# @lc code=start
class Solution:
    """
        # 前綴後綴和 prefix and suffix
        # 計算每個位置的 前綴Y 和 後綴N
    """
    def bestClosingTime(self, customers: str) -> int:

        """
            1. 遍歷3次
            Time: O(n)
        """
        # 
        # n = len(customers)
        # lst = list(customers)
        # ans = 0
        # res = float('inf')
        # pre = [0] * (n+1)
        # suf = [0] * (n+1)
        # for i in range(1, n+1):
        #     pre[i] = pre[i-1] + (lst[i-1] == 'N')
        # for i in range(n-1, -1, -1):
        #     suf[i] = suf[i+1] + (lst[i] == 'Y')
        # for i in range(n+1):
        #     if (pre[i] + suf[i]) < res:
        #         res = pre[i] + suf[i]
        #         ans = i
        # return ans

        """
            2. 遍歷2次
        """
        ans = 0
        # 以時間0的後綴Y為初始值，且時間0的前綴N為0
        res = cost = customers.count('Y')
        # 遍歷一次，計算每個時間點的 前綴N 和 後綴Y 的變動情況
        for t, ch in enumerate(customers, 1):
            if ch == 'N': # 前綴N增加
                cost += 1
                continue
            else: # 後綴Y減少
                cost -= 1
            if cost < res:
                cost = res
                ans = t
        return ans

# @lc code=end


if __name__ == '__main__':
    sol = Solution()
    print(sol.bestClosingTime("YYNY"))
    print(sol.bestClosingTime("NNNNN"))
    print(sol.bestClosingTime("YYYY"))