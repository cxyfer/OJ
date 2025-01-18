/*
 * @lc app=leetcode.cn id=1579 lang=cpp
 *
 * [1579] 保证图可完全遍历
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class DSU {
public:
    vector<int> pa, sz;
    int cnt;
    DSU(int n) {
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
    int maxNumEdgesToRemove(int n, vector<vector<int>>& edges) {
        vector<vector<pair<int, int>>> lst(3);
        for (auto& e : edges){
            lst[e[0]-1].emplace_back(e[1]-1, e[2]-1);
        }
        int ans = 0;
        DSU uf1(n), uf2(n);
        for (auto& e : lst[2]){
            int u = e.first, v = e.second;
            if (!uf1.unionSet(u, v) || !uf2.unionSet(u, v))
                ans++;
        }
        for (auto& e : lst[0]){
            int u = e.first, v = e.second;
            if (!uf1.unionSet(u, v))
                ans++;
        }
        for (auto& e : lst[1]){
            int u = e.first, v = e.second;
            if (!uf2.unionSet(u, v))
                ans++;
        }
        return uf1.cnt == 1 && uf2.cnt == 1 ? ans : -1;
    }
};
// @lc code=end
