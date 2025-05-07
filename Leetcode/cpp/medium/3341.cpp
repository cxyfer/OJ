/*
 * @lc app=leetcode.cn id=3341 lang=cpp
 * @lcpr version=30204
 *
 * [3341] 到达最后一个房间的最少时间 I
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
struct Node {
    int x, y, t;
    bool operator<(const Node &other) const {
        return t > other.t;
    }
};

class Solution {
private:
    vector<pair<int, int>> DIR = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
public:
    int minTimeToReach(vector<vector<int>>& moveTime) {
        int n = moveTime.size(), m = moveTime[0].size();
        vector<vector<int>> dist(n, vector<int>(m, INT_MAX));
        dist[0][0] = 0;
        priority_queue<Node> pq;
        pq.emplace(0, 0, 0);  // (x, y, t)
        while (!pq.empty()) {
            auto [x, y, t] = pq.top(); pq.pop();
            if (x == n - 1 && y == m - 1) return t;
            if (t > dist[x][y]) continue;
            for (auto& [dx, dy] : DIR) {
                int nx = x + dx, ny = y + dy;
                if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                int nt = max(t, moveTime[nx][ny]) + 1;
                if (nt < dist[nx][ny]) {
                    dist[nx][ny] = nt;
                    pq.emplace(nx, ny, nt);
                }
            }
        }
        return -1;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [[0,4],[4,4]]\n
// @lcpr case=end

// @lcpr case=start
// [[0,0,0],[0,0,0]]\n
// @lcpr case=end

// @lcpr case=start
// [[0,1],[1,2]]\n
// @lcpr case=end

 */

