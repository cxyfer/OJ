
#
# @lc app=leetcode.cn id=2736 lang=python3
#
# [2736] 最大和查询
#
from preImport import *
# @lc code=start
class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        ans = [-1] * len(queries)
        pairs = sorted(((num1, num2) for num1, num2 in zip(nums1, nums2)), key=lambda x: -x[0])
        n = len(pairs)
        j = 0
        st = []
        for i, (x, y) in sorted(enumerate(queries), key=lambda x: -x[1][0]):
            while j < n and pairs[j][0] >= x:  # 下面只需关心 ay (a[j][1])
                ax, ay = pairs[j]
                while st and st[-1][1] <= ax + ay:  # ay >= st[-1][0]
                    st.pop()
                if not st or st[-1][0] < ay:
                    st.append((ay, ax + ay))
                j += 1
            p = bisect_left(st, (y,))
            if p < len(st):
                ans[i] = st[p][1]
        return ans
# @lc code=end

