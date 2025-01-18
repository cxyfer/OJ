/*
 * @lc app=leetcode.cn id=2812 lang=cpp
 *
 * [2812] 找出最安全路径
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    /*
        1. 多源BFS + DFS/BFS/DSU + Binary Search
            首先用多源BFS計算每個點到最近的 1 的曼哈頓距離，因此問題可以轉換成，是否存在一條從起點到終點的路徑，使得每個點到最近的 1 的距離都 >= x。
            而最大化最小值，可以想到二分答案，對於每個 x ，檢查是否存在這樣的路徑。
        2. 多源BFS + DSU
            在 1. 預處理到最近的 1 的曼哈頓距離的基礎上優化，可以從最大距離開始枚舉距離 x ，將所有距離 >= x 的點合併，
            若起點和終點在同一個集合中，則存在一條路徑，使得每個點到最近的 1 的距離都 >= x。
            由於每個點只會被合併一次，因此若將DSU的時間複雜度視為 O(1) ，則時間複雜度約為 O(n^2) 。
    */
    int maximumSafenessFactor(vector<vector<int>>& grid) {
        // return solve1(grid);
        return solve2(grid);
    }
    int solve1(vector<vector<int>>& grid) {
        int n = grid.size();
        int DIR[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        // 多源BFS計算每個點到最近的 1 的曼哈頓距離
        vector<vector<int>> dist(n, vector<int>(n, -1));
        queue<tuple<int, int, int>> q;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    dist[i][j] = 0;
                    q.push({i, j, 0});
                }
            }
        }
        while (!q.empty()) {
            auto t = q.front(); q.pop();
            int i = get<0>(t), j = get<1>(t), d = get<2>(t);
            for (int k = 0; k < 4; k++) {
                int nx = i + DIR[k][0], ny = j + DIR[k][1];
                if (0 <= nx && nx < n && 0 <= ny && ny < n && dist[nx][ny] == -1) {
                    dist[nx][ny] = d + 1;
                    q.push({nx, ny, d+1});
                }
            }
        }
        // 對答案二分，這裡使用BFS來檢查是否存在一條路徑
        function<bool(int)> check = [&](int x) {
            if (dist[0][0] < x) return false;
            vector<vector<bool>> visited(n, vector<bool>(n, false));
            queue<pair<int, int>> q;
            q.push({0, 0});
            visited[0][0] = true;
            while (!q.empty()) {
                auto p = q.front(); q.pop();
                int i = p.first, j = p.second;
                if (i == n-1 && j == n-1) return true;
                for (int k = 0; k < 4; k++) {
                    int nx = i + DIR[k][0], ny = j + DIR[k][1];
                    if (0 <= nx && nx < n && 0 <= ny && ny < n && !visited[nx][ny] && dist[nx][ny] >= x) {
                        visited[nx][ny] = true;
                        q.push({nx, ny});
                    }
                }
            }
            return false;
        };
        int left = 0, right = (n << 1) - 2; // [0, 2n-2]
        while (left <= right) { // 區間不為空
            int mid = (left + right) / 2;
            if (check(mid)) left = mid + 1;
            else right = mid - 1;
        }
        return right;
    }
    int solve2(vector<vector<int>>& grid) {
        int n = grid.size();
        int DIR[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        // 多源BFS計算每個點到最近的 1 的曼哈頓距離
        vector<vector<int>> dist(n, vector<int>(n, -1));
        queue<tuple<int, int, int>> q;
        int mx = 0; // 最大距離
        unordered_map<int, vector<pair<int, int>>> groups; // 保存距離到點的對應關係
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    dist[i][j] = 0;
                    q.push({i, j, 0});
                    groups[0].push_back({i, j});
                }
            }
        }
        while (!q.empty()) {
            auto t = q.front(); q.pop();
            int i = get<0>(t), j = get<1>(t), d = get<2>(t);
            for (int k = 0; k < 4; k++) {
                int nx = i + DIR[k][0], ny = j + DIR[k][1];
                if (0 <= nx && nx < n && 0 <= ny && ny < n && dist[nx][ny] == -1) {
                    dist[nx][ny] = d + 1;
                    q.push({nx, ny, d+1});
                    groups[d+1].push_back({nx, ny});
                    mx = max(mx, d+1);
                }
            }
        }
        // Disjoint Set Union (DSU)
        vector<int> fa(n*n);
        iota(fa.begin(), fa.end(), 0); // init
        function<int(int)> find = [&](int x) {
            return x == fa[x] ? x : fa[x] = find(fa[x]);
        };
        function<void(int, int)> union_ = [&](int x, int y) {
            x = find(x), y = find(y);
            if (x != y) fa[x] = y;
        };
        // 從最大距離開始枚舉 x
        for (int d = mx; d >= 0; d--) {
            for (auto p : groups[d]) {
                int i = p.first, j = p.second;
                for (int k = 0; k < 4; k++) {
                    int nx = i + DIR[k][0], ny = j + DIR[k][1];
                    if (0 <= nx && nx < n && 0 <= ny && ny < n && dist[nx][ny] >= d) { // 周圍有距離 >= x 的點，則使其連通
                        union_(i*n+j, nx*n+ny);
                    }
                }
                if (find(0) == find(n*n-1)) return d;
            }
        }
        return 0;
    }
};
// @lc code=end

