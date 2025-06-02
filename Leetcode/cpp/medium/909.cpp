/*
 * @lc app=leetcode.cn id=909 lang=cpp
 * @lcpr version=30204
 *
 * [909] 蛇梯棋
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int snakesAndLadders(vector<vector<int>>& board) {
        int n = board.size();
        auto get_pos = [&](int u) -> pair<int, int> {
            int r = (u - 1) / n, c = (u - 1) % n;
            if (r % 2 == 1) c = n - 1 - c;
            return {n - 1 - r, c};
        };
        queue<pair<int, int>> q;
        q.push({1, 0});
        vector<bool> vis(n * n + 1);
        vis[1] = true;
        while (!q.empty()) {
            int u = q.front().first, d = q.front().second;
            q.pop();
            auto [r, c] = get_pos(u);
            if (board[r][c] != -1) {
                u = board[r][c];
            }
            if (u == n * n) return d;
            for (int v = u + 1; v <= min(u + 6, n * n); v++) {
                if (vis[v]) continue;
                vis[v] = true;
                q.push({v, d + 1});
            }
        }
        return -1;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]\n
// @lcpr case=end

// @lcpr case=start
// [[-1,-1],[-1,3]]\n
// @lcpr case=end

 */

