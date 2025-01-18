# @algorithm @lc id=2473 lang=python3 
# @title max-sum-of-a-pair-with-equal-sum-of-digits


from en.Python3.mod.preImport import *
# @test([18,43,36,13,7])=54
# @test([10,12,19,14])=-1
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        cnt = defaultdict(list)
        for num in nums:
            sod = sum(map(int, list(str(num))))
            cnt[sod].append(num)
        ans = -1
        for key in cnt:
            if len(cnt[key]) < 2:
                continue
            cnt[key].sort(reverse=True)
            ans = max(ans, cnt[key][0] + cnt[key][1])
        return ans