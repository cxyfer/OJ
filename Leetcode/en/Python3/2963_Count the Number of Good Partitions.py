# @algorithm @lc id=3212 lang=python3 
# @title count-the-number-of-good-partitions


from en.Python3.mod.preImport import *
# @test([1,2,3,4])=8
# @test([1,1,1,1])=1
# @test([1,2,1,3])=2
class Solution:
    """
        相同數字若重複出現，必須在同一個區間內
    """
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        # 區間
        n = len(nums)
        cnt = defaultdict(list) # 每個數字出現的最左和最右位置
        for i, num in enumerate(nums):
            cnt[num].append(i)

        # 區間合併
        intervals = []
        for num, indices in cnt.items():
            intervals.append((indices[0], indices[-1]))
        intervals.sort(key=lambda x: x[0])

        res = []
        for x, y in intervals:
            if not res or x > res[-1][1]: # not overlap
                res.append([x, y])
            else:
                res[-1][1] = max(res[-1][1], y) # overlap, update interval
        return pow(2, len(res) - 1, MOD)