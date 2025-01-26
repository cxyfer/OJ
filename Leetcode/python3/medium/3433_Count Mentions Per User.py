#
# @lc app=leetcode id=3433 lang=python3
# @lcpr version=30204
#
# [3433] Count Mentions Per User
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countMentions(self, n: int, events: List[List[str]]) -> List[int]:
        ans = [0] * n
        off = [0] * n
        events.sort(key=lambda x: (int(x[1]), 0 if x[0] == 'OFFLINE' else 1))
        for (typ, ts, data) in events:
            ts = int(ts)
            if typ == "OFFLINE":
                uid = int(data)
                off[uid] = ts + 60
            elif typ == "MESSAGE":
                if data == "ALL":
                    for uid in range(n):
                        ans[uid] += 1
                elif data == "HERE":
                    for uid in range(n):
                        if off[uid] <= ts:
                            ans[uid] += 1
                else:
                    for uid in map(lambda x: int(x[2:]), data.split()):
                        ans[uid] += 1
        return ans
# @lc code=end

sol = Solution()
print(sol.countMentions(2, [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]])) # [2,2]  
print(sol.countMentions(2, [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","12","ALL"]])) # [2,2]
print(sol.countMentions(2, [["OFFLINE","10","0"],["MESSAGE","12","HERE"]])) # [0,1]
print(sol.countMentions(3, [["MESSAGE","2","HERE"],["OFFLINE","2","1"],["OFFLINE","1","0"],["MESSAGE","61","HERE"]])) # [1,0,2]

#
# @lcpr case=start
# 2\n[["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","12","ALL"]]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[["OFFLINE","10","0"],["MESSAGE","12","HERE"]]\n
# @lcpr case=end

#

