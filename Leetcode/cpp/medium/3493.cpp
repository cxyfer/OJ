/*
 * @lc app=leetcode.cn id=3493 lang=cpp
 * @lcpr version=30204
 *
 * [3493] 属性图
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
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

class Solution {
public:
    int numberOfComponents(vector<vector<int>>& properties, int k) {
        int n = properties.size(), m = properties[0].size();
        UnionFind uf(n);
        vector<unordered_set<int>> sets(n);
        for (int i = 0; i < n; i++)
            sets[i] = unordered_set<int>(properties[i].begin(), properties[i].end());
    
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int cnt = 0;
                for (auto &x : sets[i])
                    if (sets[j].count(x))
                        cnt++;
                if (cnt >= k)
                    uf.unionSet(i, j);
            }
        }
        return uf.cnt;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [[1,2],[1,1],[3,4],[4,5],[5,6],[7,7]]\n1\n
// @lcpr case=end

// @lcpr case=start
// [[1,2,3],[2,3,4],[4,3,5]]\n2\n
// @lcpr case=end

// @lcpr case=start
// [[1,1],[1,1]]\n2\n
// @lcpr case=end

 */

