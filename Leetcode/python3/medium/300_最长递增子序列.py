#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#
from preImport import *
# @lc code=start
class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.solve3(nums)
    """
        1. Dynamic Programming (in Textbook)
        這裡使用了在 CLRS Exercise 14.4-5 的 Solution 中給出的方法：
        令 X 為原序列，Y 為原序列排序後所得的序列，
        X 和 Y 的 Longest Common Subsequence (LCS)，就是 X 的 Longest Increasing Subsequence (LIS)。
        這裡把 X 擺在 左邊，Y 擺在 上面，方便理解。

        ***但直接使用這種方法，若遇到重複的數字的情況，就會出錯，因此要先去重。***
    """
    def solve1(self, X: List[int]) -> int:
        Y = sorted(list(set(X))) # Y 為 X 排序後的序列，要去重
        n, m = len(X), len(Y)

        # 1. 用 dp 和 label 來紀錄 LCS
        dp = [[0] * (m+1) for _ in range(n+1)] # dp[i][j] 表示 X[:i] 和 Y[:j] 的 LCS 長度
        label = [[""] * (m+1) for _ in range(n+1)] # label[i][j] 表示 X[:i] 和 Y[:j] 的 LCS 的最後一個元素的方向
        for i in range(1, n+1):
            for j in range(1, m+1):
                if X[i-1] == Y[j-1]: # X[i-1] 和 Y[j-1] 相等，可以接在 X[:i-1] 和 Y[:j-1] 的 LCS 的末尾
                    dp[i][j] = dp[i-1][j-1] + 1 
                    label[i][j] = "↖"
                elif dp[i-1][j] >= dp[i][j-1]:
                    dp[i][j] = dp[i-1][j]
                    label[i][j] = "↑"
                else:
                    dp[i][j] = dp[i][j-1]
                    label[i][j] = "←"
        
        # 2. 從 dp 中找到最長的 LCS 長度，並從 label 中重構出對應的 LCS (由後往前)
        res = [-1] * dp[n][m] # LCS 長度為 dp[n][m]
        i, j = n, m
        while i > 0 and j > 0:
            if label[i][j] == "↖":
                res[dp[i][j]-1] = X[i-1]
                i -= 1
                j -= 1
            elif label[i][j] == "↑":
                i -= 1
            else:
                j -= 1
        print(res) # LIS
        return dp[n][m] # LIS 長度

    """
        2. Dynamic Programming
        dp[i] 表示以 nums[i] 結尾的 LIS 長度
        dp[i] = max(dp[i], dp[j] + 1) for j in [0, i) if nums[j] < nums[i]
        Time: O(n^2)
        Space: O(n)
    """
    def solve2(self, nums: List[int]) -> int:
        n = len(nums)
        # 1. 用 dp 和 prev 來紀錄 LIS
        prev = [-1] * n # prev[i] 表示以 nums[i] 結尾的 LIS 的前一個位置
        dp = [1] * n # dp[i] 表示以 nums[i] 結尾的 LIS 長度
        for i in range(1, n): # 枚舉所有位置 i
            for j in range(i): # 枚舉 i 前面的所有位置 j
                if nums[j] < nums[i]: # nums[i] 可以接在 nums[j] 後面
                    if dp[j] + 1 > dp[i]: # 若可以得到更大的LIS長度，更新 dp[i] 和 prev[i]
                        dp[i] = dp[j] + 1
                        prev[i] = j

        # 2. 從 dp 中找到最長的 LIS 長度，並從 prev 中重構出對應的 LIS (由後往前)
        max_len = max(dp)
        res = [-1] * max_len
        for i in range(n-1, -1, -1):
            if dp[i] == max_len:
                cur = i
                idx = max_len - 1
                while cur != -1:
                    res[idx] = nums[cur]
                    cur = prev[cur]
                    idx -= 1
                break
        print(res)
        return max_len
    """
        3. Greedy + Binary Search
        即 15.4-6 ⋆ 要求的 O(nlogn) 時間複雜度的算法
        Robinson-Schensted-Knuth Algorithm

        - tail[i] 表示 長度為 i+1 的 LIS 的最後一個元素的最小值，初始化 tail[0] = nums[0]
            - 需要注意的是，tail 並不是一個 LIS，只是用來計算 LIS 長度的輔助陣列
        - pos[i] 紀錄 nums[i] 在 LIS 中的第幾個位置
    """
    def solve3(self, nums: List[int]) -> int:
        n = len(nums)

        tail = [nums[0]] # tail[i] 表示 長度為 i+1 的 LIS 的最後一個元素的最小值，初始化 tail[0] = nums[0]
        pos = [0] * n # pos[i] 紀錄 nums[i] 在 LIS 中的第幾個位置

        for i in range(1, n):
            if nums[i] > tail[-1]: # nums[i] 可以接在 tail 的末尾，並構成更長的 LIS
                tail.append(nums[i]) # tail 長度加 1
                # 這裡可以直接跳過，因為 nums[i] > tail[-1]，所以二分查找的結果一定是新增的元素的位置
                # 但不加結果是相同的，只是多了一次不必要的二分查找
                pos[i] = len(tail) - 1
                continue

            # 在 tail 中二分查找，找到第一個大於等於 nums[i] 的元素，並將其更新為 nums[i]
            # left = bisect_left(tail, nums[i])
            left = 0
            right = len(tail) - 1
            while left <= right: # [left, right]
                mid = (left + right) // 2
                if tail[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid -1
            tail[left] = nums[i]
            pos[i] = left

        # 2. 根據 pos 重構 LIS
        res = [-1] * len(tail)
        j = len(tail) - 1
        for i in range(n-1, -1, -1):
            if pos[i] == j:
                res[j] = nums[i]
                j -= 1
        print(res)
        return len(tail)
# @lc code=end
sol = Solution()
print(sol.lengthOfLIS([10,9,2,5,3,7,101,18])) # 4
print(sol.lengthOfLIS([0,1,0,3,2,3])) # 4
print(sol.lengthOfLIS([7,7,7,7,7,7,7])) # 1
print(sol.lengthOfLIS([4,1,7,5,2,5,8,4])) # 4
