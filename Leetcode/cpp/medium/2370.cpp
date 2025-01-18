/*
 * @lc app=leetcode id=2370 lang=cpp
 * @lcpr version=30122
 *
 * [2370] Longest Ideal Subsequence
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int longestIdealString(string s, int k) {
        int n = s.size(), x, mx;
        int dp[26]={0};
        for(int i=0; i<n; i++){
            x = s[i]-'a';
            mx = 0;
            for(int j=max(0, x-k); j<min(26, x+k+1); j++){
                mx = max(mx, dp[j]);
            }
            dp[x] = mx+1;
        }
        mx = 0;
        for(int i=0; i<26; i++) mx = max(mx, dp[i]);
        return mx;
    }
};
// @lc code=end



/*
// @lcpr case=start
// "acfgbd"\n2\n
// @lcpr case=end

// @lcpr case=start
// "abcd"\n3\n
// @lcpr case=end

 */

