#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def partitionLabels(self, s: str) -> List[int]:
        pos = defaultdict(list)
        for i, ch in enumerate(s):
            pos[ch].append(i)

        intervals = [[p[0], p[-1]] for p in pos.values() if p]
        # intervals.sort()  # 如果用雜湊表的話其實不用排序，加入順序就是排序好的
        merged = []
        for st, ed in intervals:
            if not merged or merged[-1][1] < st:
                merged.append([st, ed])
            else:
                merged[-1][1] = max(merged[-1][1], ed)
        return [ed - st + 1 for st, ed in merged]
    
class Solution2:
    def partitionLabels(self, s: str) -> List[int]:
        last = [-1] * 26
        for i, ch in enumerate(s):
            last[ord(ch) - ord('a')] = i
        
        ans = []
        st = ed = 0
        for i, ch in enumerate(s):
            ed = max(ed, last[ord(ch) - ord('a')])
            if i == ed:
                ans.append(ed - st + 1)
                st = ed + 1
        return ans

# Solution = Solution1
Solution = Solution2
# @lc code=end

sol = Solution()
print(sol.partitionLabels("ababcbacadefegdehijhklij"))  # [9,7,8]
print(sol.partitionLabels("eccbbbbdec"))  # [10]