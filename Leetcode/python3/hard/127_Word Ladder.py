#
# @lc app=leetcode id=127 lang=python3
# @lcpr version=30204
#
# [127] Word Ladder
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
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



#
# @lcpr case=start
# "hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]\n
# @lcpr case=end

# @lcpr case=start
# "hit"\n"cog"\n["hot","dot","dog","lot","log"]\n
# @lcpr case=end

#

