#
# @lc app=leetcode.cn id=1282 lang=python3
#
# [1282] 用户分组
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hash_map = defaultdict(list)
        ans = []
        for i, size in enumerate(groupSizes):
            hash_map[size].append(i)
            if len(hash_map[size]) == size:
                ans.append(hash_map.pop(size))
        return ans

# @lc code=end

