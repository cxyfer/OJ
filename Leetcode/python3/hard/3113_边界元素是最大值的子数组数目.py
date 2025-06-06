#
# @lc app=leetcode.cn id=3113 lang=python3
#
# [3113] 边界元素是最大值的子数组数目
#
from preImport import *
# @lc code=start
class Solution:
    """
        單調堆疊(Monotonic Stack)
        枚舉右端點，若在遍歷陣列時遇到 x ，會使左邊比 x 小的數無法組成合法的子陣列。
        故可以維護一個單調遞減的堆疊。
    """
    def numberOfSubarrays(self, nums: List[int]) -> int:
        ans = 0
        st = [] # 單調遞減堆疊，(element, count)
        for x in nums:
            while st and x > st[-1][0]: # 維持單調遞減性質
                st.pop()
            if st and x == st[-1][0]: # 堆疊頂端元素與 x 相同，則可以構成符合條件的子陣列
                _, cnt = st.pop()
                ans += cnt + 1 # 以 x 為右端點的子陣列數量(包含長度為1的子陣列)
                st.append([x, cnt+1])
            else: # 堆疊頂端元素比 x 大，則只能構成長度為1的子陣列
                ans += 1
                st.append([x, 1])
        return ans
# @lc code=end
sol = Solution()
print(sol.numberOfSubarrays([1,4,3,3,2])) # 6
print(sol.numberOfSubarrays([3,3,3])) # 6
print(sol.numberOfSubarrays([1])) # 1
