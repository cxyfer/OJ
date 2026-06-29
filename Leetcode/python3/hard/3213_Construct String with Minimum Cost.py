#
# @lc app=leetcode id=3213 lang=python3
# @lcpr version=30204
#
# [3213] Construct String with Minimum Cost
#


# @lcpr-template-start
from regex import B

from preImport import *
import random
# @lcpr-template-end
# @lc code=start
fmin = lambda x, y: x if x < y else y


class Node:
    def __init__(self):
        self.child = [None] * 26
        self.fail = None  # fail pointer
        self.last = None  # suffix link，用來快速跳到一定是某個 word 結尾的節點
        # self.is_end = False
        # self.depth = depth
        self.length = 0  # 可以取代 is_end 和 depth
        self.cost = float("inf")


class AhoCorasick:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str, cost: int):
        node = self.root
        for ch in word:
            c = ord(ch) - ord("a")
            if not node.child[c]:
                node.child[c] = Node()
            node = node.child[c]
        node.length = len(word)
        node.cost = min(node.cost, cost)  # 避免相同單字有不同 cost

    def build(self):  # O(|Σ|N)，N 是節點數；若 |Σ|=26 視為常數，則為 O(N) = O(L)
        self.root.fail = self.root.last = self.root
        # BFS
        q = deque()
        for i, v in enumerate(self.root.child):
            if v is None:
                # 添加虛擬子節點
                self.root.child[i] = self.root
            else:
                v.fail = v.last = self.root
                q.append(v)
        while q:
            u = q.popleft()
            for i, v in enumerate(u.child):
                if v is None:
                    # 添加虛擬子節點
                    u.child[i] = u.fail.child[i]
                else:
                    # 失配位置
                    v.fail = u.fail.child[i]
                    # 上一個一定是某個 word 結尾的節點
                    v.last = v.fail if v.fail.length else v.fail.last
                    q.append(v)


class Solution1:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        ac = AhoCorasick()
        for word, cost in zip(words, costs):
            ac.insert(word, cost)
        ac.build()

        n = len(target)
        f = [0] + [float("inf")] * n
        node = ac.root
        for i, ch in enumerate(target, 1):
            node = node.child[ord(ch) - ord("a")]
            if node.length:  # 匹配到了一個盡可能長的 words[k]
                f[i] = min(f[i], f[i - node.length] + node.cost)
            # 沿著 last 往上尋找，可能可以找到其餘更短，但可以使成本更小的 words[k]
            temp = node.last
            while temp != ac.root:
                f[i] = min(f[i], f[i - temp.length] + temp.cost)
                temp = temp.last
        return f[n] if f[n] != float("inf") else -1


class Solution2:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        n = len(target)

        MOD = 1_070_777_777
        BASE = random.randint(int(8e8), int(9e8))
        # MOD = int(1e18) + 3
        # BASE = randint(int(8e17), int(9e17))

        P = [1] + [0] * n  # P[i] = BASE^i % MOD
        H = [0] * (n + 1)  # H[i] = hash(s[:i])
        for i, b in enumerate(target):
            # 預計算所有冪次
            P[i + 1] = P[i] * BASE % MOD
            # 預計算所有前綴雜湊
            H[i + 1] = (H[i] * BASE + ord(b)) % MOD

        # 每個 word[i] 的雜湊值 -> 最小成本
        min_cost = defaultdict(lambda: float("inf"))
        for word, cost in zip(words, costs):
            h = 0
            for b in word:
                h = (h * BASE + ord(b)) % MOD
            min_cost[h] = min(min_cost[h], cost)

        # 有 O(√L) 個不同的長度
        sorted_lens = sorted(set(map(len, words)))

        f = [0] + [float("inf")] * n
        for i in range(1, n + 1):
            for ln in sorted_lens:
                if ln > i:
                    break
                h = (H[i] - H[i - ln] * P[ln]) % MOD
                # f[i] = min(f[i], f[i - sz] + min_cost[h])
                tmp = f[i - ln] + min_cost[h]
                if tmp < f[i]:
                    f[i] = tmp
        return -1 if f[n] == float("inf") else f[n]


Solution = Solution1
# Solution = Solution2
# @lc code=end

sol = Solution()
print(sol.minimumCost("abcdef", ["abdef", "abc", "d", "def", "ef"], [100, 1, 1, 10, 5]))  # 7

#
# @lcpr case=start
# "abcdef"\n["abdef","abc","d","def","ef"]\n[100,1,1,10,5]\n
# @lcpr case=end

# @lcpr case=start
# "aaaa"\n["z","zz","zzz"]\n[1,10,100]\n
# @lcpr case=end

#

