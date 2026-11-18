/*
 * @lc app=leetcode id=2914 lang=cpp
 *
 * [2914] Minimum Number of Changes to Make Binary String Beautiful
 */

// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int minChanges(string s) {
        int n = s.size();
        int ans = 0;
        for (int i = 0; i < n; i += 2) {
            ans += (s[i] ^ s[i + 1]);
        }
        return ans;
    }
};
// @lc code=end
