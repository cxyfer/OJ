/*
 * @lc app=leetcode.cn id=2320 lang=cpp
 *
 * [2320] 统计放置房子的方式数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
const int MOD = 1e9 + 7;
class Solution {
public:
    int countHousePlacements(int n) {
        // return solve1(n);
        return solve2(n);
    }
    int solve1(int n) {
        vector<int> dp(n+1, 0);
        dp[0] = 1; dp[1] = 2;
        for (int i = 2; i <= n; i++) {
            dp[i] = (dp[i-1] + dp[i-2]) % MOD;
        }
        return (long long) dp[n] * dp[n] % MOD;
    }
    int solve2(int n) {
        int f0 = 1, f1 = 2, f2;
        for (int i = 2; i <= n; i++) {
            f2 = (f0 + f1) % MOD;
            f0 = f1;
            f1 = f2;
        }
        return (long long) f1 * f1 % MOD;
    }
};
// @lc code=end

int main(int argc, char const *argv[])
{
    Solution sol;
    cout << sol.countHousePlacements(1000) << endl; // 500478595
    return 0;
}


