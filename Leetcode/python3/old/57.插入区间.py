#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        # 1. Greedy
        # Smilar to 56. Merge Intervals
        # Time: O(nlogn) # sort
        """
        # ans = []
        # intervals.append(newInterval)
        # intervals.sort(key=lambda x: x[0])
        # for x, y in intervals:
        #     if not ans or x > ans[-1][1]: # not overlap
        #         ans.append([x, y])
        #     else:
        #         ans[-1][1] = max(ans[-1][1], y) # overlap, update interval
        # return ans
    
        """
        # 2. Simulation
        # 因為 會當發生重疊的情況一定是和newInterval重疊，所以可以只檢查newInterval就好，不用加入後排序(nlogn)
        # Time: O(n)
        """

        left, right = newInterval
        added = False
        ans = []
        for li, ri in intervals:
            # case 1. 原本的區間在newInterval的左側且無交集
            if ri < left: 
                ans.append([li, ri])   
            # case 2. 原本的區間在newInterval的右側且無交集
            elif li > right:
                if not added: # 如果newInterval還沒加入ans，就先加入
                    ans.append([left, right])
                    added = True
                ans.append([li, ri])
            # case 3. 與newInterval有交集，計算新的區間，但這個區間可能還會再被更新，所以先不加入ans
            else:
                left = min(left, li)
                right = max(right, ri)
        # 考慮不存在case2.，即所有區間都在newInterval的左側的情況，所以newInterval還沒加入ans，要把他加入
        if not added: 
            ans.append([left, right])
        return ans

# @lc code=end

