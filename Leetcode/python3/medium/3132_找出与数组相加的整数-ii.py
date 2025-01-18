#
# @lc app=leetcode.cn id=3132 lang=python3
#
# [3132] 找出与数组相加的整数 II
#
from preImport import *
# @lc code=start
class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return self.solve1(nums1, nums2)
        # return self.solve2(nums1, nums2)
    """
        1. 賽時寫法 Counter
        由於兩個陣列的差為刪除兩個數後的最大值，因此可以考慮 nums1 刪除後的最大值 mx1 ，就能求出差值。
        題目保證有解，因此 mx1 只可能是 nums1 排序後最大的三個數字的其一，故分別考慮計算其「缺失」的數字數量即可。
    """
    def solve1(self, nums1: List[int], nums2: List[int]) -> int:
        cnt1, cnt2 = Counter(nums1), Counter(nums2)
        k1 = sorted(cnt1.keys())
        mx2 = max(cnt2.keys())

        def check(x): # 若差是 x ，其「缺失」的數字數量
            res = 0
            for k, v in cnt1.items():
                if k + x not in cnt2: # 全部缺失
                    res += v
                elif cnt2[k + x] < v: # 部分缺失
                    res += v - cnt2[k + x]
            return res
        
        for i in range(3): # 0, 1, 2
            mx1 = k1[-1-i] # -1, -2, -3 ，nums1 中最大的數是 mx1 ，則根據題意只有三種可能
            x = mx2 - mx1
            if check(x) == 2-i: # 缺失的數字數量依次必須是 2, 1, 0
                return x
            cnt1[mx1] -= 1
            if cnt1[mx1] == 0:
                del cnt1[mx1]
        return -1
    """
        2. 靈神寫法 Two Pointers
        同樣是枚舉保留中的最小值，但是改成計算「存在」的數字數量是否等同於 nums2 的長度。
    """
    def solve2(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        for k in range(2, -1, -1): # 由於是計算「存在」的數字數量，因此必須從較大的數字開始
            x = nums2[0] - nums1[k] 
            i = j = 0
            while i < len(nums1) and j < len(nums2): # 同向雙指標
                if nums1[i] + x == nums2[j]:
                    j += 1
                i += 1
            if j == len(nums2):
                return x
        return -1
# @lc code=end
sol = Solution()
print(sol.minimumAddedInteger([4,20,16,12,8], [14,18,10])) # -2
print(sol.minimumAddedInteger([3,5,5,3], [7,7])) # 2
print(sol.minimumAddedInteger([7,2,6,8,7], [7,6,5])) # -1
print(sol.minimumAddedInteger([9,4,3,9,4], [7,8,8])) # 4
print(sol.minimumAddedInteger([9,10,0,7,8,0], [0,8,7,0])) # 0

