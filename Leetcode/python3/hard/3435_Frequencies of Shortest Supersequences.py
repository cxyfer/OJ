#
# @lc app=leetcode id=3435 lang=python3
# @lcpr version=30204
#
# [3435] Frequencies of Shortest Supersequences
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def supersequences(self, words: list[str]) -> list[list[int]]:
        sigma = sorted(set(ch for word in words for ch in word))
        m = len(sigma)
        mp = {ch: i for i, ch in enumerate(sigma)}

        g = [[] for _ in range(m)]
        for word in words:
            u, v = mp[word[0]], mp[word[1]]
            g[u].append(v) # 添加邊，表示 word[0] 必須在 word[1] 前面

        def get_len(mask: int) -> int:
            """計算 SCS 長度，mask 為位元遮罩，標記哪些字母出現兩次"""
            return mask.bit_count() + m

        def check(mask: int) -> bool:
            """檢查當前字母出現次數分配 (mask) 是否能產生有效的 SCS"""
            indeg = [0] * m
            for u in range(m):
                if mask & (1 << u):  # 如果字母 u 出現兩次，則跳過
                    continue
                for v in g[u]:
                    if mask & (1 << v): # 如果字母 v 出現兩次，則跳過
                        continue
                    indeg[v] += 1 # u 必須在 v 前面

            q = deque()
            for u in range(m):
                if indeg[u] == 0 and not (mask & (1 << u)): # 入度為 0 且只出現一次的字母加入佇列
                    q.append(u)

            cnt = 0 # 紀錄拓撲排序訪問的節點數量
            while q:
                u = q.popleft()
                cnt += 1
                for v in g[u]:
                    if mask & (1 << v): # 如果字母 v 出現兩次，則跳過
                        continue
                    indeg[v] -= 1
                    if indeg[v] == 0:
                        q.append(v)

            # 拓撲排序成功，表示存在合法的排列
            return cnt == m - mask.bit_count() # 檢查訪問的節點數是否等於預期只出現一次的字母數量

        mn = float('inf')
        masks = [] # 儲存所有有效且長度最短的 mask

        # 使用 bitmask枚舉所有可能的字母出現次數組合
        for i in range(1 << m):
            if not check(i):
                continue
            ln = get_len(i)
            if ln < mn:
                masks = []
                mn = ln
            if ln == mn:
                masks.append(i)

        ans = []
        for mask in masks:
            cnt = [0] * 26
            for j in range(m):
                idx = ord(sigma[j]) - ord('a')
                cnt[idx] = 2 if mask & (1 << j) else 1
            ans.append(cnt)
        return ans
# @lc code=end

#
# @lcpr case=start
# ["ab","ba"]\n
# @lcpr case=end

# @lcpr case=start
# ["aa","ac"]\n
# @lcpr case=end

# @lcpr case=start
# ["aa","bb","cc"]\n
# @lcpr case=end

# @lcpr case=start
# ["jq","iq","qj","qi","ij"]\n
# @lcpr case=end

# @lcpr case=start
# ["mh","hm","mr","rm","hr","rh"]\n
# @lcpr case=end

# @lcpr case=start
# ["gg","gq","qg"]\n
# @lcpr case=end


