/*
 * @lc app=leetcode.cn id=1733 lang=cpp
 * @lcpr version=30204
 *
 * [1733] 需要教语言的最少人数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <ranges>
class Solution {
public:
    int minimumTeachings(int n, vector<vector<int>>& languages, vector<vector<int>>& friendships) {
        int m = languages.size();
        // Convert to bitset
        vector<bitset<501>> lang(m);
        for (int i = 0; i < m; i++)
            for (auto &l : languages[i])
                lang[i][l] = 1;
    
        // Count the number of people who can speak each language
        vector<int> cnt(n + 1);
        vector<bool> vis(m);
        int tot = 0;
        auto add = [&](int x) {
            if (vis[x]) return;
            vis[x] = true;
            tot++;
            for (auto &l : languages[x])
                cnt[l]++;
        };
        // Add pairs that don't have common languages
        for (auto &f : friendships) {
            int u = f[0] - 1, v = f[1] - 1;
            if ((lang[u] & lang[v]).any()) continue;
            add(u);
            add(v);
        }
        return tot - ranges::max(cnt);
    }
};
// @lc code=end



/*
// @lcpr case=start
// 2\n[[1],[2],[1,2]]\n[[1,2],[1,3],[2,3]]\n
// @lcpr case=end

// @lcpr case=start
// 3\n[[2],[1,3],[1,2],[3]]\n[[1,4],[1,2],[3,4],[2,3]]\n
// @lcpr case=end

 */

