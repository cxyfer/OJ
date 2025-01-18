# @algorithm @lc id=332 lang=python3 
# @title reconstruct-itinerary


from en.Python3.mod.preImport import *
# @test([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]])=["JFK","MUC","LHR","SFO","SJC"]
# @test([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])=["JFK","ATL","JFK","SFO","ATL","SFO"]
class Solution:
    """
        Backtracking
    """
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        n = len(tickets)
        tickets.sort() # 先排序，這樣一旦找到第一個可行路徑，一定是字母排序最小的
        Graph = defaultdict(list)
        for idx, (u, v) in enumerate(tickets):
            Graph[u].append((idx, v))
        ans = []
        path = ['JFK']
        visited = set()

        def backtracking(i: int) -> bool:
            if len(path) == n + 1:
                ans.append(path.copy())
                return
            for idx, v in Graph[path[i]]:
                if idx not in visited:
                    visited.add(idx)
                    path.append(v)
                    backtracking(i + 1)
                    path.pop()
                    visited.remove(idx)
                    if ans: # 如果已經找到一個可行路徑，就不用再找了
                        return
        backtracking(0)
        return ans[0]