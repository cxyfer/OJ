#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#
from preImport import *
# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # return self.solve1(beginWord, endWord, wordList)
        return self.solve2(beginWord, endWord, wordList)
    """
        1. Floyd-Warshall
        TLE
    """
    def solve1(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(wordList)

        if endWord not in wordList:
            return 0
        
        def isConnect(w1, w2):
            cnt = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    cnt += 1
            return cnt == 1
        
        g = defaultdict(lambda: defaultdict(lambda: float("inf")))

        g[beginWord][beginWord] = 0
        for w in wordList:
            g[w][w] = 0
        for i, w1 in enumerate(wordList):
            if isConnect(beginWord, w1):
                g[beginWord][w1] = 1
                g[w1][beginWord] = 1
            for j in range(i+1, n):
                w2 = wordList[j]
                if isConnect(w1, w2):
                    g[w1][w2] = 1
                    g[w2][w1] = 1
        
        # Floyd-Warshall
        for k in g.keys():
            for i in g.keys():
                if g[i][k] == float("inf"):
                    continue
                for j in g.keys():
                    g[i][j] = min(g[i][j], g[i][k] + g[k][j])
        return g[beginWord][endWord] + 1 if g[beginWord][endWord] != float("inf") else 0
    """
        2. primitive BFS
        TLE
    """
    def solve2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(wordList)

        def isConnect(w1, w2):
            cnt = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    cnt += 1
            return cnt == 1
        
        g = defaultdict(list)
        for i, w1 in enumerate(wordList):
            if isConnect(beginWord, w1):
                g[beginWord].append(w1)
                g[w1].append(beginWord)
            for j in range(i+1, n):
                w2 = wordList[j]
                if isConnect(w1, w2):
                    g[w1].append(w2)
                    g[w2].append(w1)
                    
        q = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)
        while q:
            w, d = q.popleft()
            if w == endWord:
                return d
            for nxt in g[w]:
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, d+1))
        return 0
# @lc code=end

sol = Solution()
print(sol.ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"])) # 5
print(sol.ladderLength("hit","cog",["hot","dot","dog","lot","log"])) # 0
print(sol.ladderLength("ymain","oecij",["ymann","yycrj","oecij","ymcnj","yzcrj","yycij","xecij","yecij","ymanj","yzcnj","ymain"])) # 10