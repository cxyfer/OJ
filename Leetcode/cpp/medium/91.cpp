/*
 * @lc app=leetcode id=91 lang=cpp
 * @lcpr version=30112
 *
 * [91] Decode Ways
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int numDecodings(string s) {
        int n = s.size();
        vector<int> dp(n+1, 0);
        dp[0] = 1;
        dp[1] = (s[0] == '0') ? 0 : 1;
        for(int i=2; i<=n; i++){
            if (s[i-1] != '0'){
                dp[i] += dp[i-1];
            }
            if (s[i-2] == '1' || (s[i-2] == '2' && s[i-1] <= '6')){
                dp[i] += dp[i-2];
            }
        }
        return dp[n];
    }
};
// @lc code=end



/*
// @lcpr case=start
// "12"\n
// @lcpr case=end

// @lcpr case=start
// "226"\n
// @lcpr case=end

// @lcpr case=start
// "06"\n
// @lcpr case=end

 */

