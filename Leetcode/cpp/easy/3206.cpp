/*
 * @lc app=leetcode.cn id=3206 lang=cpp
 *
 * [3206] 交替组 I
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int numberOfAlternatingGroups(vector<int>& colors) {
        int n = colors.size();
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (colors[i] == colors[(i + 2) % n] && colors[i] != colors[(i + 1) % n]) ans++;
        }
        return ans;
    }
};
// @lc code=end

