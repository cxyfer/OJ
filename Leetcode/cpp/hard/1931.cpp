/*
 * @lc app=leetcode.cn id=1931 lang=cpp
 * @lcpr version=30204
 *
 * [1931] 用三种不同颜色为网格涂色
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
private:
    const int MOD = 1e9 + 7;
public:
    int colorTheGrid(int m, int n) {
        vector<int> pow3(m + 1);
        pow3[0] = 1;
        for (int i = 1; i <= m; i++) pow3[i] = pow3[i - 1] * 3;

        vector<int> states;
        for (int s = 0; s < pow3[m]; s++) {
            bool ok = true;
            for (int k = 0; k < m - 1; k++) {
                if ((s / pow3[k]) % 3 == (s / pow3[k + 1]) % 3) {
                    ok = false;
                    break;
                }
            }
            if (ok) states.push_back(s);
        }

        int ns = states.size();
        vector<vector<int>> nexts(ns);
        for (int i = 0; i < ns; i++) {
            for (int j = 0; j < i; j++) {
                bool ok = true;
                for (int k = 0; k < m; k++) {
                    if ((states[i] / pow3[k]) % 3 == (states[j] / pow3[k]) % 3) {
                        ok = false;
                        break;
                    }
                }
                if (ok) {
                    nexts[i].push_back(j);
                    nexts[j].push_back(i);
                }
            }
        }

        vector<vector<int>> memo(n, vector<int>(ns, -1));
        auto dfs = [&](this auto &&dfs, int i, int s) -> int {
            if (i == n) return 1;
            if (memo[i][s] != -1) return memo[i][s];
            int res = 0;
            for (int j : nexts[s])
                res = (res + dfs(i + 1, j)) % MOD;
            return memo[i][s] = res;
        };

        int ans = 0;
        for (int j = 0; j < ns; j++)
            ans = (ans + dfs(1, j)) % MOD;
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// 1\n1\n
// @lcpr case=end

// @lcpr case=start
// 1\n2\n
// @lcpr case=end

// @lcpr case=start
// 5\n5\n
// @lcpr case=end

 */

