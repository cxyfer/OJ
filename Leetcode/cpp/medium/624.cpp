/*
 * @lc app=leetcode.cn id=624 lang=cpp
 *
 * [624] 数组列表中的最大距离
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int maxDistance(vector<vector<int>>& arrays) {
        int n = arrays.size();
        int mn = arrays[0].front(), mx = arrays[0].back();
        int ans = -1e9;
        for (int i = 1; i < n; i++) {
            int a = arrays[i].front(), b = arrays[i].back();
            ans = max(ans, max(mx - a, b - mn));
            mn = min(mn, a);
            mx = max(mx, b);
        }
        return ans;
    }
};
// @lc code=end