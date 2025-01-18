# @algorithm @lc id=943 lang=python3 
# @title sum-of-subarray-minimums


from en.Python3.mod.preImport import *
# @test([3,1,2,4])=17
# @test([11,81,94,43,3])=444
class Solution:
    """
        貢獻 + Monotonic Stack
        用單調棧來找到每個數字左邊和右邊第一個比他小的數字
        為避免重複計算，將右邊界設為「小於等於」
    """
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)

        # left[i] 為左側「嚴格小於」 arr[i] 的最近元素位置
        left = [-1] * n # 不存在時為 -1
        st = []
        for i in range(n):
            while st and arr[st[-1]] >= arr[i]: # 不滿足嚴格小於，移除
                st.pop()
            if st:
                left[i] = st[-1]
            st.append(i)
        # right[i] 為右側「小於等於」 arr[i] 的最近元素位置
        right = [n] * n # 不存在時為 n
        st = []
        for i in range(n-1, -1, -1):
            while st and arr[st[-1]] > arr[i]: # 不滿足小於等於，移除
                st.pop()
            if st:
                right[i] = st[-1]
            st.append(i)

        ans = 0
        for i, (x, L, R) in enumerate(zip(arr, left, right)):
            ans += x * (i - L) * (R - i) # 累加x的貢獻
        return ans % (10 ** 9 + 7)