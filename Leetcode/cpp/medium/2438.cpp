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
using LL = long long;
class Solution {
public:
    int MOD = 1e9 + 7;
    vector<int> productQueries(int n, vector<vector<int>>& queries) {
        int lb;
        vector<int> s(1, 0);
        while (n){
            lb = n & -n;
            s.push_back(s.back() + bit_length(lb) - 1);
            n ^= lb;
        }
        vector<int> ans(queries.size(), 0);
        for (int i = 0; i < queries.size(); i++) {
            ans[i] = qpow(2, s[queries[i][1] + 1] - s[queries[i][0]]);
        }
        return ans;
    }
    int bit_length(int n) {
        int res = 0;
        while (n) {
            n >>= 1;
            res++;
        }
        return res;
    }
    LL qpow(LL x, int n) {
        LL res = 1;
        while (n) {
            if (n & 1) res = (res * x) % MOD;
            x = (x * x) % MOD;
            n >>= 1;
        }
        return res;
    }
};
// @lc code=end



/*
// @lcpr case=start
// 15\n[[0,1],[2,2],[0,3]]\n
// @lcpr case=end

// @lcpr case=start
// 2\n[[0,0]]\n
// @lcpr case=end

 */

