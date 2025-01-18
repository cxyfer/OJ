#
# @lc app=leetcode.cn id=1361 lang=python3
#
# [1361] 验证二叉树
#
from preImport import *
# @lc code=start
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # 1. calculate indegree
        indegree = [0] * n
        for u in leftChild:
            if u != -1:
                indegree[u] += 1
        for u in rightChild:
            if u != -1:
                indegree[u] += 1
        # 2. find root
        root = -1
        for i in range(n):
            if indegree[i] == 0:
                root = i
                break
        if root == -1:
            return False
        # 3. bfs
        seen = set([root])
        q = deque([root])
        while q:
            u = q.popleft()
            for v in [leftChild[u], rightChild[u]]: # left and right child
                if v == -1:
                    continue
                if v in seen: # visit 2 times, cycle
                    return False
                seen.add(v)
                q.append(v)
        return len(seen) == n
# @lc code=end

