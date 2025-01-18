#
# @lc app=leetcode id=3213 lang=python3
# @lcpr version=30204
#
# [3213] Construct String with Minimum Cost
#


# @lcpr-template-start
from preImport import *
import random
# @lcpr-template-end
# @lc code=start
class Node:
    def __init__(self):
        self.child = [None] * 26
        # self.is_end = False
        # self.depth = depth
        self.length = 0 # 若只保存在結尾的節點，可以省略 is_end
        self.fail = None # fail pointer
        self.last = None # suffix link，用來快速跳到一定是某個 word 結尾的節點
        self.cost = float('inf')

class AhoCorasick:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str, cost: int):
        node = self.root
        for ch in word: 
            idx = ord(ch) - ord('a')
            if not node.child[idx]:
                node.child[idx] = Node()
            node = node.child[idx]
        node.length = len(word)
        node.cost = min(node.cost, cost) # 避免相同單字有不同 cost

    def build(self):
        self.root.fail = self.root.last = self.root
        q = deque()
        # 先處理第一層的 fail 和 last
        for i, child in enumerate(self.root.child):
            if child is None: # 添加虛擬子節點
                self.root.child[i] = self.root
            else:
                child.fail = child.last = self.root # 第一層的失配指標都指向 root
                q.append(child)
        # BFS
        while q:
            node = q.popleft()
            for i, child in enumerate(node.child):
                if child is None: # 添加虛擬子節點
                    # 虛擬子節點 node.child[i] 和 node.fail.child[i] 是同一個
                    # 方便失配時直接跳到下一個可能匹配的位置（但不一定是某個 words[k] 的最后一個字母）
                    node.child[i] = node.fail.child[i]
                    continue
                # 計算失配位置
                child.fail = node.fail.child[i] 
                # 計算 suffix link，沿著 fail 指標找到一定是某個 word 結尾的節點
                child.last = child.fail if child.fail.length else child.fail.last
                q.append(child)

class Solution1:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        ac = AhoCorasick()
        for word, cost in zip(words, costs):
            ac.insert(word, cost)
        ac.build()

        n = len(target)
        f = [0] + [float('inf')] * n
        node = ac.root
        for i, ch in enumerate(target, 1):
            # 如果沒有匹配，相當於移動到 fail 的 child[ch]
            node = node.child[ord(ch) - ord('a')]
            if node.length: # 匹配到了一個盡可能長的 words[k]
                f[i] = min(f[i], f[i - node.length] + node.cost)
            # 沿著 last 鏈上尋找，可能可以找到其餘更短，但可以使成本更小的 words[k]
            match_node = node.last
            while match_node != ac.root:
                # f[i] = min(f[i], f[i - match_node.length] + match_node.cost)
                tmp = f[i - match_node.length] + match_node.cost
                if tmp < f[i]:
                    f[i] = tmp
                match_node = match_node.last
        return -1 if f[n] == float('inf') else f[n]

class Solution2:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        n = len(target)

        MOD = 1_070_777_777
        BASE = random.randint(8 * 10 ** 8, 9 * 10 ** 8)
        # MOD = int(1e18) + random.randint(0, int(1e9))
        # BASE = 233 + random.randint(0, 1000)

        P = [1] + [0] * n  # P[i] = BASE^i % MOD
        H = [0] * (n + 1)  # H[i] = hash(s[:i])
        for i, b in enumerate(target):
            # 預計算所有冪次
            P[i + 1] = P[i] * BASE % MOD
            # 預計算所有前綴雜湊
            H[i + 1] = (H[i] * BASE + ord(b)) % MOD 

        # 每個 word[i] 的雜湊值 -> 最小成本
        min_cost = defaultdict(lambda: float('inf'))
        for word, cost in zip(words, costs):
            h = 0
            for b in word:
                h = (h * BASE + ord(b)) % MOD
            min_cost[h] = min(min_cost[h], cost)

        # 有 O(√L) 個不同的長度
        sorted_lens = sorted(set(map(len, words)))

        f = [0] + [float('inf')] * n
        for i in range(1, n + 1):
            for sz in sorted_lens:
                if sz > i:
                    break
                sub_hash = (H[i] - H[i - sz] * P[sz]) % MOD
                # f[i] = min(f[i], f[i - sz] + min_cost[sub_hash])
                tmp = f[i - sz] + min_cost[sub_hash]
                if tmp < f[i]:
                    f[i] = tmp
        return -1 if f[n] == float('inf') else f[n]
    
# class Solution(Solution1):
class Solution(Solution2):
    pass
# @lc code=end



#
# @lcpr case=start
# "abcdef"\n["abdef","abc","d","def","ef"]\n[100,1,1,10,5]\n
# @lcpr case=end

# @lcpr case=start
# "aaaa"\n["z","zz","zzz"]\n[1,10,100]\n
# @lcpr case=end

#

