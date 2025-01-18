/*
 * @lc app=leetcode.cn id=685 lang=cpp
 *
 * [685] 冗余连接 II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start

/*
假設多的邊為 (u, v) ，則有以下 3 種情況：
1. v 是根節點，此時會出現環，但 v 只有 1 個父節點
2. v 是 u 除了根節點以外的某個祖先，此時會出現環，且 v 存在 2 個父節點
3. 其餘情況，此時 v 會有 2 個父節點
*/

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

class Solution {
public:
    vector<int> findRedundantDirectedConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        vector<vector<int>> rg(n + 1); // 反圖
        int mark = -1; // 記錄有兩個父節點的節點
        for (int i = 0; i < n; i++) {
            int u = edges[i][0], v = edges[i][1];
            rg[v].push_back(i); // 記錄節點 v 的邊索引
            if (rg[v].size() == 2) mark = v; // 出現 Case 2 或 Case 3
        }
        UnionFind uf(n + 1);
        for (int i = 0; i < n; i++) {
            int u = edges[i][0], v = edges[i][1];
            // 出現 Case 2 或 Case 3，此時跳過指向 mark 的第二條邊
            if (mark != -1 && i == rg[mark][1]) continue;
            if (!uf.unionSet(u, v)) { // 有環
                if (mark == -1) return edges[i]; // Case 1
                else return edges[rg[mark][0]]; // Case 2a
            }
        }
        return edges[rg[mark][1]]; // Case 2b or Case 3
    }
};
// @lc code=end
