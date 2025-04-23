/*
 * @lc app=leetcode.cn id=2338 lang=cpp
 * @lcpr version=30204
 *
 * [2338] 统计理想数组的数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
const int MOD = 1e9 + 7;
const int MAX_N = 1e4;
const int MAX_E = ceil(log2(MAX_N));

vector<int> LPF(MAX_N + 1, 0);
vector<unordered_map<int, int>> EXP(MAX_N + 1);
vector<vector<int>> COMB(MAX_N + MAX_E + 1, vector<int>(MAX_E + 1, 0));

auto init = []() {
    for (int i = 2; i <= MAX_N; i++) {
        if (LPF[i] == 0) {
            LPF[i] = i;
            for (int j = i * i; j <= MAX_N; j += i)
                if (LPF[j] == 0) LPF[j] = i;
        }
    }
    for (int x = 2; x <= MAX_N; x++) {
        int t = x;
        while (t > 1) {
            int p = LPF[t];
            EXP[x][p]++;
            t /= p;
        }
    }

    for (int i = 0; i <= MAX_N + MAX_E; i++) {
        COMB[i][0] = 1;
        for (int j = 1; j <= min(i, MAX_E); j++)
            COMB[i][j] = (COMB[i - 1][j] + COMB[i - 1][j - 1]) % MOD;
    }
    return 0;
}();

class Solution {
public:
    int idealArrays(int n, int maxValue) {
        long long ans = 0;
        for (int x = 1; x <= maxValue; x++) {
            long long cur = 1;
            for (auto [p, e] : EXP[x])
                cur = cur * COMB[n + e - 1][e] % MOD;
            ans = (ans + cur) % MOD;
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// 2\n5\n
// @lcpr case=end

// @lcpr case=start
// 5\n3\n
// @lcpr case=end

 */

