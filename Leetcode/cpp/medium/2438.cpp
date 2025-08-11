/*
 * @lc app=leetcode id=2438 lang=cpp
 * @lcpr version=30122
 *
 * [2438] Range Product Queries of Powers
 */

// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
const int MOD = 1e9 + 7;
using LL = long long;

LL qpow(LL x, int n, int mod) {
    LL res = 1;
    while (n) {
        if (n & 1) res = res * x % mod;
        x = x * x % mod;
        n >>= 1;
    }
    return res;
}

class Solution1a {
public:
    vector<int> productQueries(int n, vector<vector<int>>& queries) {
        vector<int> s(1, 0);
        while (n) {
            int lb = n & -n;
            s.push_back(s.back() + bit_width(static_cast<unsigned int>(lb)) - 1);
            n ^= lb;
        }
        vector<int> ans(queries.size(), 0);
        for (int i = 0; i < queries.size(); i++)
            ans[i] = qpow(2, s[queries[i][1] + 1] - s[queries[i][0]], MOD);
        return ans;
    }
};

vector<int> pow2(500, 1);
auto init = []() {
    for (int i = 1; i < 500; i++) pow2[i] = pow2[i - 1] * 2 % MOD;
    return 0;
}();

class Solution1b {
public:
    vector<int> productQueries(int n, vector<vector<int>>& queries) {
        vector<int> s(1, 0);
        while (n) {
            int lb = n & -n;
            s.push_back(s.back() + bit_width(static_cast<unsigned int>(lb)) - 1);
            n ^= lb;
        }
        vector<int> ans(queries.size(), 0);
        for (int i = 0; i < queries.size(); i++)
            ans[i] = pow2[s[queries[i][1] + 1] - s[queries[i][0]]];
        return ans;
    }
};

class Solution2a {
public:
    vector<int> productQueries(int n, vector<vector<int>>& queries) {
        vector<LL> s(1, 1);
        while (n) {
            int lb = n & -n;
            s.push_back(s.back() * lb % MOD);
            n ^= lb;
        }
        vector<LL> inv(s.size());
        for (int i = 0; i < s.size(); i++) inv[i] = qpow(s[i], MOD - 2, MOD);
        vector<int> ans(queries.size(), 0);
        for (int i = 0; i < queries.size(); i++)
            ans[i] = s[queries[i][1] + 1] * inv[queries[i][0]] % MOD;
        return ans;
    }
};

class Solution2b {
public:
    vector<int> productQueries(int n, vector<vector<int>>& queries) {
        vector<int> powers;
        while (n) {
            int lb = n & -n;
            powers.push_back(lb);
            n ^= lb;
        }
        int m = powers.size();
        vector<LL> s(m + 1, 1), inv(m);
        for (int i = 1; i <= m; i++) s[i] = s[i - 1] * powers[i - 1] % MOD;
        inv[m - 1] = qpow(s[m - 1], MOD - 2, MOD);
        for (int i = m - 2; i >= 0; i--) inv[i] = inv[i + 1] * powers[i] % MOD;
        vector<int> ans(queries.size(), 0);
        for (int i = 0; i < queries.size(); i++)
            ans[i] = s[queries[i][1] + 1] * inv[queries[i][0]] % MOD;
        return ans;
    }
};

// using Solution = Solution1a;
using Solution = Solution1b;
// using Solution = Solution2a;
// using Solution = Solution2b;
// @lc code=end

/*
// @lcpr case=start
// 15\n[[0,1],[2,2],[0,3]]\n
// @lcpr case=end

// @lcpr case=start
// 2\n[[0,0]]\n
// @lcpr case=end

 */
