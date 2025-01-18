#
# @lc app=leetcode.cn id=2007 lang=python3
#
# [2007] 从双倍数组中还原原数组
#
from preImport import *
# @lc code=start
class Solution:
    """
        1. Sort + Counter / Queue
    """
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # return self.solve1a(changed)
        # return self.solve1b(changed)
        return self.solve2(changed)
    """
        1. Sort + Counter
    """
    def solve1a(self, changed: List[int]) -> List[int]:
        ans = []
        changed.sort()
        cnt = Counter()
        for x in changed:
            if not cnt[x]: # 不存在 x/2 ，代表 x 是原始數字
                ans.append(x)
                cnt[x*2] += 1 # x*2 應該要在 changed 中，標記需要一個 x*2
            else: # 存在 x/2
                cnt[x] -= 1
        return ans if all(x == 0 for x in cnt.values()) else []
    """
        1b. Sort + Queue
        由於已經按照由小到大排序，故先被標記的數字會先出現
    """
    def solve1b(self, changed: List[int]) -> List[int]:
        ans = []
        changed.sort()
        q = deque()
        for x in changed:
            if not q or x != q[0]: # 不存在 x/2 ，代表 x 是原始數字
                if q and q[0] < x: # q 中存在不可能配對成功的數字 q[0] ，可以提早結束
                    return []
                ans.append(x)
                q.append(x*2)
            else: # 存在 x/2
                q.popleft()
        return ans if not q else []
    """
        2. 直接配對
        若 x/2 在 changed 中，則應該從 x/2 開始配對，以此類推。
        故**不用排序**，直接遍歷 changed ，檢查 x/2 是否在 changed 中即可。
        找到不存在 x/2 的 x 後，開始配對 x, 2x, 4x, 8x, ...
        Time: O(n)
    """
    def solve2(self, changed: List[int]) -> List[int]:
        cnt = Counter(changed)
        cnt0 = cnt[0]
        del cnt[0]
        if cnt0 & 1:
            return []
        ans = [0] * (cnt0 // 2)

        visited = set()
        for x in cnt:
            if x in visited: # x 已經配對過
                continue
            if x % 2 == 0 and x // 2 in cnt: # x/2 在 cnt 中，遍歷到 x/2 再處理即可
                continue
            while x in cnt: # 開始配對 x, 2x, 4x, 8x, ...
                cnt_x = cnt[x]
                if cnt_x > cnt[x * 2]: # 至少要有 cnt_x 個 2x 才能配對
                    return []
                ans.extend([x] * cnt_x) # 配對 x 和 2x
                visited.add(x)
                if cnt_x < cnt[x * 2]: # 還有剩下的 2x，繼續配對 2x
                    cnt[x * 2] -= cnt_x
                    x *= 2
                else: # 2x 也配對完成，從 4x 開始
                    visited.add(x * 2)
                    x *= 4
        return ans
# @lc code=end
sol = Solution()
print(sol.findOriginalArray([1,3,4,2,6,8])) # [1,3,4]
print(sol.findOriginalArray([6,3,0,1])) # []
print(sol.findOriginalArray([1])) # []
print(sol.findOriginalArray([1,2,3,4])) # []
print(sol.findOriginalArray([0,0,0,0])) # [0,0]