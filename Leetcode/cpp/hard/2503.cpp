/*
 * @lc app=leetcode.cn id=2503 lang=cpp
 * @lcpr version=30204
 *
 * [2503] 矩阵查询可获得的最大分数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
/*
 * 1. Offline Query + Kruskal's Algorithm
 *  - 由於是網格圖，因此事前連邊時，只連右和下即可
 *  - 這種寫法支援查詢時從任何一格開始，且也能改變判斷條件，例如改成當兩格之和 <= v 時連邊等
 * 2. Offline Query + Heap
 *  - 由於起點是 (0, 0)，且邊的 weight 是兩格的 max value，所以可以維護未訪問點的 value 即可
*/
// @lc code=start
class UnionFind {
public:
    vector<int> pa, sz;
    int cnt;
    UnionFind(int n) {
        pa.resize(n);
        iota(pa.begin(), pa.end(), 0);
        sz.assign(n, 1);
        cnt = n;
    }
    int find(int x) {
        return pa[x] == x ? x : pa[x] = find(pa[x]);
    }
    bool unionSet(int x, int y) {
        x = find(x), y = find(y);
        if (x == y) return false;
        if (sz[x] < sz[y]) swap(x, y);
        pa[y] = x;
        sz[x] += sz[y];
        cnt--;
        return true;
    }
};

class Solution1 {
public:
    vector<int> maxPoints(vector<vector<int>>& grid, vector<int>& queries) {
        int m = grid.size(), n = grid[0].size(), q = queries.size();

        // Offline Query
        vector<int> qidxs(q);
        iota(qidxs.begin(), qidxs.end(), 0);
        sort(qidxs.begin(), qidxs.end(), [&](int i, int j) {
            return queries[i] < queries[j];
        });

        // Kruskal's Algorithm: create edges
        UnionFind uf(m * n);
        vector<tuple<int, int, int>> edges;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // Only need to connect right and down
                if (i + 1 < m) edges.emplace_back(max(grid[i][j], grid[i + 1][j]), i * n + j, (i + 1) * n + j);
                if (j + 1 < n) edges.emplace_back(max(grid[i][j], grid[i][j + 1]), i * n + j, i * n + j + 1);
            }
        }
        sort(edges.begin(), edges.end());

        // Kruskal's Algorithm: union edges
        int idx = 0;
        vector<int> ans(q);
        for (auto& qi : qidxs) {
            int query = queries[qi];
            while (idx < edges.size() && get<0>(edges[idx]) < query) {
                auto [w, x, y] = edges[idx++];
                uf.unionSet(x, y);
            }
            ans[qi] = grid[0][0] < query ? uf.sz[uf.find(0)] : 0;  // answer the query
        }
        return ans;
    }
};

struct Node {
    int val, x, y;
    bool operator<(const Node& other) const {
        return val > other.val;
    }
};

class Solution2 {
    const vector<pair<int, int>> dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
public:
    vector<int> maxPoints(vector<vector<int>>& grid, vector<int>& queries) {
        int m = grid.size(), n = grid[0].size(), q = queries.size();

        // Offline Query
        vector<int> qidxs(q);
        iota(qidxs.begin(), qidxs.end(), 0);
        sort(qidxs.begin(), qidxs.end(), [&](int i, int j) {
            return queries[i] < queries[j];
        });

        // Min Heap to find the minimum value
        priority_queue<Node> pq;
        pq.emplace(grid[0][0], 0, 0);
        vector<vector<bool>> vis(m, vector<bool>(n, false));
        vis[0][0] = true;

        vector<int> ans(q);
        int cnt = 0; // count of visited nodes
        for (auto& qi : qidxs) {
            int query = queries[qi];
            // pop all nodes with value < query and visit them
            while (!pq.empty() && pq.top().val < query) {
                auto [_, x, y] = pq.top(); pq.pop();
                cnt++;
                // push the adjacent nodes into the heap
                for (auto [dx, dy] : dirs) {    
                    int nx = x + dx, ny = y + dy;
                    if (nx < 0 || nx >= m || ny < 0 || ny >= n || vis[nx][ny]) continue;
                    vis[nx][ny] = true;
                    pq.emplace(grid[nx][ny], nx, ny);
                }
            }
            ans[qi] = cnt;  // answer the query
        }
        return ans;
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end



/*
// @lcpr case=start
// [[1,2,3],[2,5,7],[3,5,1]]\n[5,6,2]\n
// @lcpr case=end

// @lcpr case=start
// [[5,2,1],[1,1,2]]\n[3]\n
// @lcpr case=end

 */

