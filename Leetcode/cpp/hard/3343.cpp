/*
 * @lc app=leetcode.cn id=3343 lang=cpp
 *
 * [3343] 统计平衡排列的数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
using LL = long long;
const int MOD = 1e9 + 7;
const int MAXN = 80;

vector<LL> fact(MAXN + 1), invf(MAXN + 1);
vector<vector<LL>> comb(MAXN + 1, vector<LL>(MAXN + 1, 0));

LL pow(LL x, int n) {
    LL res = 1;
    while (n) {
        if (n & 1) res = res * x % MOD;
        x = x * x % MOD;
        n >>= 1;
    }
    return res;
}

auto init = [] {
    fact[0] = 1;
    for (int i = 1; i <= MAXN; i++) {
        fact[i] = fact[i - 1] * i % MOD;
    }
    invf[MAXN] = pow(fact[MAXN], MOD - 2);
    for (int i = MAXN; i; i--) {
        invf[i - 1] = invf[i] * i % MOD;
    }
    for (int i = 0; i <= MAXN; i++) {
        comb[i][0] = 1;
        for (int j = 1; j <= i; j++) {
            comb[i][j] = (comb[i - 1][j] + comb[i - 1][j - 1]) % MOD;
        }
    }
    return 0;
}();

class Solution {
public:
    int countBalancedPermutations(string num) {
        int n = num.size();
        vector<int> cnt(10);
        for (char ch : num) {
            cnt[ch - '0']++;
        }
        int n_e = (n + 1) / 2, n_o = n / 2;
        LL s = 0;
        for (int i = 0; i < 10; i++) {
            s += (cnt[i] * i);
        }
        if (s & 1) return 0;
        vector<vector<vector<LL>>> memo(10, vector<vector<LL>>(n_e + 1, vector<LL>(s / 2 + 1, -1)));
        auto dfs = [&](auto &&dfs, int d, int left_e, int left_s) -> LL {
            if (d == 10) {
                return (left_e == 0 && left_s == 0) ? 1 : 0;
            }
            LL &res = memo[d][left_e][left_s];
            if (res != -1) return res;
            res = 0;
            for (int k = 0; k <= min(cnt[d], left_e); k++) {
                if (k * d > left_s) break;
                res = (res + (dfs(dfs, d + 1, left_e - k, left_s - k * d) * comb[cnt[d]][k]) % MOD) % MOD;
            }
            return res;
        };
        LL ans = dfs(dfs, 0, n_e, s / 2);
        ans = ans * fact[n_e] % MOD;
        ans = ans * fact[n_o] % MOD;
        for (int d = 0; d < 10; d++) {
            ans = ans * invf[cnt[d]] % MOD;
        }
        return ans;
    }
};
// @lc code=end

int main() {
    Solution sol = Solution();
    cout << sol.countBalancedPermutations("123") << endl; // 2
    cout << sol.countBalancedPermutations("112") << endl; // 1
    cout << sol.countBalancedPermutations("12345") << endl; // 0
    return 0;
}