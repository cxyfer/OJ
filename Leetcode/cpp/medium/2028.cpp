/*
 * @lc app=leetcode.cn id=2028 lang=cpp
 *
 * [2028] 找出缺失的观测数据
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<int> missingRolls(vector<int>& rolls, int mean, int n) {
        int m = rolls.size();
        int s = mean * (m + n); // 缺失值的總和
        for (int x : rolls) s -= x;
        if (s < n || s > 6 * n) return {}; // 無法滿足條件
        vector<int> ans(n, s / n);
        for (int i = 0; i < s % n; i++) ans[i]++;
        return ans;
    }
};
// @lc code=end

