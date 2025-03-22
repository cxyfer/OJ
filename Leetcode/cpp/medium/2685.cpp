/*
 * @lc app=leetcode.cn id=2685 lang=cpp
 * @lcpr version=30204
 *
 * [2685] 统计完全连通分量的数量
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int countCompleteComponents(int n, vector<vector<int>>& edges) {
        vector<int> pa(n), sz(n, 1), cnt(n);
        iota(pa.begin(), pa.end(), 0);

        auto find = [&](int x) -> int {
            while (x != pa[x]) x = pa[x] = pa[pa[x]];
            return x;
        };

        for (auto& e : edges) {
            int fx = find(e[0]), fy = find(e[1]);
            cnt[fx]++;
            if (fx == fy) continue;
            if (sz[fx] < sz[fy]) swap(fx, fy);
            pa[fy] = fx;
            sz[fx] += sz[fy];
            cnt[fx] += cnt[fy];
        }

        int ans = 0;
        vector<bool> vis(n, false);
        for (int x = 0; x < n; x++) {
            int fx = find(x);
            if (vis[fx]) continue;
            if (sz[fx] * (sz[fx] - 1) == cnt[fx] * 2) ans++;
            vis[fx] = true;
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// 6\n[[0,1],[0,2],[1,2],[3,4]]\n
// @lcpr case=end

// @lcpr case=start
// 6\n[[0,1],[0,2],[1,2],[3,4],[3,5]]\n
// @lcpr case=end

 */

