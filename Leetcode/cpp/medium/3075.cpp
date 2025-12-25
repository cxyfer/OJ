/*
 * @lc app=leetcode.cn id=3075 lang=cpp
 *
 * [3075] 幸福值最大化的选择方案
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <ranges>

class Solution {
public:
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        ranges::sort(happiness, greater<int>());
        long long ans = 0;
        for (int i = 0; i < k; i++) {    // 選擇 k 輪
            ans += max(0, happiness[i] - i);
        }
        return ans;
    }
};
// @lc code=end

