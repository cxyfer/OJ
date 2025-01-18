# @algorithm @lc id=2839 lang=python3 
# @title maximum-sum-queries


from en.Python3.mod.preImport import *
# @test([4,3,1,2],[2,4,9,5],[[4,1],[1,3],[2,5]])=[6,10,7]
# @test([3,2,5],[2,3,4],[[4,4],[3,2],[1,1]])=[9,9,9]
# @test([2,1],[2,3],[[3,3]])=[-1]
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