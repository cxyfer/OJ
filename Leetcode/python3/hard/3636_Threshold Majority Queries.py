#
# @lc app=leetcode id=3636 lang=python3
#
# [3636] Threshold Majority Queries
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def subarrayMajority(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n, q = len(nums), len(queries)

        # 回滾莫隊 (只加不刪)
        cnt = defaultdict(int)
        min_val, max_cnt = -1, 0
        def add(x: int) -> None:
            nonlocal min_val, max_cnt
            cnt[x] += 1
            if cnt[x] > max_cnt:
                min_val = x
                max_cnt = cnt[x]
            elif cnt[x] == max_cnt:
                min_val = min(min_val, x)

        BLK_SZ = math.ceil(n / math.sqrt(q * 2))

        ans = [-1] * q
        qs = []  # (bid, l, r, th, qid)
        for qid, (l, r, th) in enumerate(queries):
            # 大區間離線，確保 l 和 r 不在同一個 block 中
            if r - l + 1 > BLK_SZ:
                qs.append((l // BLK_SZ, l, r, th, qid))
                continue
            # 小區間暴力
            for x in nums[l: r + 1]:
                add(x)
            ans[qid] = min_val if max_cnt >= th else -1
            # 重置
            cnt.clear()
            min_val, max_cnt = -1, 0

        qs.sort(key=lambda x: (x[0], x[2]))  # sort by block index and right index
        for i, (bid, ql, qr, th, qid) in enumerate(qs):
            l0 = (bid + 1) * BLK_SZ
            if i == 0 or bid > qs[i - 1][0]:  # 遍歷到一個新的 block
                r = l0  # 右端點移動的起点
                cnt.clear()
                min_val, max_cnt = -1, 0

            # 右端點從 r 向右移動到 qr（包含 qr）
            while r <= qr:
                add(nums[r])
                r += 1

            tmp_min_val, tmp_max_cnt = min_val, max_cnt
            # 左端點從 l0 向左移動到 ql（不包含 l0）
            for x in nums[ql: l0]:
                add(x)
            ans[qid] = min_val if max_cnt >= th else -1

            # 回滚
            min_val, max_cnt = tmp_min_val, tmp_max_cnt
            for x in nums[ql: l0]:
                cnt[x] -= 1

        return ans
# @lc code=end
sol = Solution()
print(sol.subarrayMajority([1,1,2,2,1,1], [[0,5,4],[0,3,3],[2,3,2]]))  # [1,-1,2]
print(sol.subarrayMajority([20,20,4], [[1,2,1],[0,0,1],[0,2,2],[2,2,1],[0,0,1]]))  # [4,20,20,4,20]