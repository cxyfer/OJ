/*
 * @lc app=leetcode.cn id=1524 lang=cpp
 *
 * [1524] 和为奇数的子数组数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
const int MOD = 1e9 + 7;
class Solution {
public:
    int numOfSubarrays(vector<int>& arr) {
        int n = arr.size();
        int ans = 0, s = 0;
        vector<int> cnt = {1, 0};  // cnt[0]: even, cnt[1]: odd
        for (int i = 0; i < n; i++) {
            s = (s + arr[i]) & 1;
            ans = (ans + cnt[s^1]) % MOD;
            cnt[s]++;
        }
        return ans;
    }
};
// @lc code=end

