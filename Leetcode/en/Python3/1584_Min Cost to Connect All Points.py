# @algorithm @lc id=1706 lang=python3 
# @title min-cost-to-connect-all-points


from en.Python3.mod.preImport import *
# @test([[0,0],[2,2],[3,10],[5,2],[7,0]])=20
# @test([[3,12],[-2,5],[-4,1]])=18
class Solution:
    """
        Minimum Spanning Tree (MST)
        1. Kruskal's algorithm
    """
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = []
        n = len(points) # number of points
        for i, j in combinations(range(n), 2):
            x1, y1 = points[i]
            x2, y2 = points[j]
            graph.append( [(i, j), abs(x1-x2)+abs(y1-y2)] )

        # Disjoint Set & Union
        parent = [i for i in range(n)]
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        # Kruskal's algorithm
        graph.sort(key=lambda x:x[1]) # sort by distance
        edge = 0
        cost = 0
        for (i, j), d in graph:
            a, b = find(i), find(j)
            if a != b: # if a, b not in the same set
                parent[b] = a
                edge += 1
                cost += d
            if edge == n-1: # if all points are connected
                break
        return cost