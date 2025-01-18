#
# @lc app=leetcode.cn id=815 lang=python3
#
# [815] 公交路线
#
from preImport import *
# @lc code=start
class Solution:
    """
        BFS
    """
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # 每個車站可以乘坐的公車
        stations = defaultdict(set)
        for i, stops in enumerate(routes):
            for stop in stops:
                stations[stop].add(i)
        # 每條公車路線可以到達的車站
        routes = [set(x) for x in routes]

        # BFS
        q = deque([(source, 0)]) # (車站, 次數)
        buses = set() # 已經坐過的的公車
        stops = set([source]) # 已經到達過的車站
        while q:
            pos, cost = q.popleft()
            if pos == target:
                return cost
            # 當前車站中尚未乘坐的公車
            for bus in stations[pos] - buses: 
                # 當前公車中尚未到達的車站
                for stop in routes[bus] - stops:
                    buses.add(bus)
                    stops.add(stop)
                    q.append((stop, cost + 1))
        return -1
# @lc code=end

