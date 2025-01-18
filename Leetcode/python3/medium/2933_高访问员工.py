#
# @lc app=leetcode.cn id=2933 lang=python3
#
# [2933] 高访问员工
#
from preImport import *
# @lc code=start
class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        cnt = defaultdict(list)

        for name, t in access_times:
            time = int(t[:2]) * 60  + int(t[2:])
            cnt[name].append(time)

        ans = []
        for name, times in cnt.items():
            times.sort()
            n = len(times)
            left = 0
            for idx, time in enumerate(times):
                while time - times[left] >= 60:
                    left += 1
                if idx-left+1 >= 3:
                    ans.append(name)
                    break
        ans.sort()
        return ans
# @lc code=end

