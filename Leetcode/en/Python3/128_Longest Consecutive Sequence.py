# @algorithm @lc id=128 lang=python3 
# @title longest-consecutive-sequence


from en.Python3.mod.preImport import *
# @test([100,4,200,1,3,2])=4
# @test([0,3,7,2,5,8,4,6,0,1])=9
class Solution:
    """
        Hash Table
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        ans = 0
        for num in hash_set: # 這邊寫 for num in nums 效率會很差
            if num-1 not in hash_set: # 確定 num 是一個連續序列的開頭   
                cur = num
                cur_len = 1
                while cur+1 in hash_set:
                    cur += 1
                    cur_len += 1
                ans = max(ans, cur_len)
        return ans