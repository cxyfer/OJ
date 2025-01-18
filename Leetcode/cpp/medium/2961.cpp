/*
 * @lc app=leetcode.cn id=2961 lang=cpp
 *
 * [2961] 双模幂运算
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<int> getGoodIndices(vector<vector<int>>& variables, int target) {
        int n = variables.size();
        vector<int> ans;
        for (int i = 0; i < n; i++) {
            int a = variables[i][0], b = variables[i][1], c = variables[i][2], m = variables[i][3];
            if (my_pow(my_pow(a, b, 10), c, m) == target) {
                ans.push_back(i);
            }
        }
        return ans;
    }
    int my_pow(int a, int b, int m) {
        int ans = 1;
        while (b) {
            if (b & 1) {
                ans = (ans * a) % m;
            }
            a = (a * a) % m;
            b >>= 1;
        }
        return ans;
    }
};
// @lc code=end