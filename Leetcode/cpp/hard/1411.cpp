/*
 * @lc app=leetcode.cn id=1411 lang=cpp
 * @lcpr version=30204
 *
 * [1411] 给 N x 3 网格图涂色的方案数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
const int MOD = 1e9 + 7;
const int M = 3;

vector<int> pow3(M + 1), states;
vector<vector<int>> nexts;

auto init = []() {
    pow3[0] = 1;
    for (int i = 1; i <= M; i++) pow3[i] = pow3[i - 1] * 3;
    for (int s = 0; s < pow3[M]; s++) {
        bool ok = true;
        for (int k = 0; k < M - 1; k++) {
            if ((s / pow3[k]) % 3 == (s / pow3[k + 1]) % 3) {
                ok = false;
                break;
            }
        }
        if (ok) states.push_back(s);
    }
    int ns = states.size();
    nexts.resize(ns);
    for (int i = 0; i < ns; i++) {
        for (int j = 0; j < i; j++) {
            bool ok = true;
            for (int k = 0; k < M; k++) {
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
    return 0;
}();

class Solution {
public:
    int numOfWays(int n) {
        vector<vector<int>> memo(n, vector<int>(states.size(), -1));
        auto dfs = [&](this auto &&dfs, int i, int s) -> int {
            if (i == n) return 1;
            if (memo[i][s] != -1) return memo[i][s];
            int res = 0;
            for (int j : nexts[s])
                res = (res + dfs(i + 1, j)) % MOD;
            return memo[i][s] = res;
        };

        int ans = 0;
        for (int j = 0; j < states.size(); j++)
            ans = (ans + dfs(1, j)) % MOD;
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// 1\n
// @lcpr case=end

// @lcpr case=start
// 2\n
// @lcpr case=end

// @lcpr case=start
// 3\n
// @lcpr case=end

// @lcpr case=start
// 7\n
// @lcpr case=end

// @lcpr case=start
// 5000\n
// @lcpr case=end

 */

