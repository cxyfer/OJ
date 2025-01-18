/*
 * @lc app=leetcode id=3185 lang=cpp
 *
 * [3185] Count Pairs That Form a Complete Day II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    long long countCompleteDayPairs(vector<int>& hours) {
        long long ans = 0;
        vector<int> cnt(24, 0);
        for (int x : hours) {
            x %= 24;
            ans += (x != 0) ? cnt[24 - x] : cnt[0]; 
            // ans += cnt[(24 - x) % 24];
            cnt[x]++;
        }
        return ans;
    }
};
// @lc code=end
