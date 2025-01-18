/*
 * @lc app=leetcode.cn id=3208 lang=cpp
 *
 * [3208] 交替组 II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int numberOfAlternatingGroups(vector<int>& colors, int k) {
        int n = colors.size();
        int ans = 0, cnt = 0;
        for (int i = 0; i < n + k - 1; i++) {
            if (i > 0 && colors[i % n] == colors[(i - 1) % n]) cnt = 1;
            else cnt += 1;
            if (cnt >= k) ans += 1;
        }
        return ans;
    }
};
// @lc code=end

