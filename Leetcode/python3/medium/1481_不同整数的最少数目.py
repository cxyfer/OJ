#
# @lc app=leetcode.cn id=1481 lang=python3
#
# [1481] 不同整数的最少数目
#
from preImport import *
# @lc code=start
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt = Counter(arr) 
        keys = sorted(cnt.keys(), key=cnt.get)
        i = 0
        while k:
            if k >= cnt[keys[i]]:
                k -= cnt[keys[i]]
                i += 1
            else:
                break
        return len(keys) - i
# @lc code=end

# @test([5,5,4],1)=1
# @test([4,3,1,1,3,3,2],3)=2
sol = Solution()
print(sol.findLeastNumOfUniqueInts([5,5,4],1)) # 1
print(sol.findLeastNumOfUniqueInts([4,3,1,1,3,3,2],3)) # 2