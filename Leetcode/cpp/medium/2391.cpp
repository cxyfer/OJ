/*
 * @lc app=leetcode.cn id=2391 lang=cpp
 *
 * [2391] 收集垃圾的最少总时间
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    /*
        Simulation + Prefix Sum(*)
    */
    int garbageCollection(vector<string>& garbage, vector<int>& travel) {
        int n = garbage.size(), n2 = travel.size();
        int ans = 0, m = 0, p = 0, g = 0;
        vector<int> pre(n2+1, 0); // prefix sum
        for (int i = 0; i < n2; ++i) pre[i+1] = pre[i] + travel[i];
        for (int i = 0; i < n; ++i) {
            ans += garbage[i].size();
            if (garbage[i].find('M') != string::npos) m = i;
            if (garbage[i].find('P') != string::npos) p = i;
            if (garbage[i].find('G') != string::npos) g = i;
        }
        return ans + pre[m] + pre[p] +  pre[g];
    }
};
// @lc code=end