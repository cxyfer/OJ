/*
 * @lc app=leetcode.cn id=2285 lang=cpp
 *
 * [2285] 道路的最大总重要性
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    long long maximumImportance(int n, vector<vector<int>>& roads) {
        vector<int> deg(n, 0);
        for (auto e : roads) {
            deg[e[0]]++;
            deg[e[1]]++;
        }
        sort(deg.begin(), deg.end());
        long long ans = 0;
        for (long long i = 1; i <= n; i++) {
            ans += i * deg[i-1];
        }
        return ans;
    }
};
// @lc code=end

