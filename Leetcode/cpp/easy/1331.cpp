/*
 * @lc app=leetcode.cn id=1331 lang=cpp
 *
 * [1331] 数组序号转换
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        int n = arr.size();
        set<int> s(arr.begin(), arr.end());
        unordered_map<int, int> rank;
        int i = 1;
        for (auto x : s) rank[x] = i++;
        vector<int> ans(n);
        for (int i = 0; i < n; i++) ans[i] = rank[arr[i]];
        return ans;
    }
};
// @lc code=end

