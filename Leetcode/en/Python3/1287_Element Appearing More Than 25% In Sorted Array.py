# @algorithm @lc id=1221 lang=python3 
# @title element-appearing-more-than-25-in-sorted-array


from en.Python3.mod.preImport import *
# @test([1,2,2,6,6,6,6,7,10])=6
# @test([1,1])=1
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # return Counter(arr).most_common(1)[0][0]
        n = len(arr)
        span = n // 4 + 1 # 每隔 span 個元素檢查一次
        for i in range(0, n, span):
            l = bisect_left(arr, arr[i])
            r = bisect_right(arr, arr[i])
            if r - l >= span:
                return arr[i]
        return -1
