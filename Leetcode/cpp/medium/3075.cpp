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
class Solution {
public:
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        sort(happiness.begin(), happiness.end(), greater<int>()); // 由大到小排序
        long long ans = 0;
        for (int i = 0; i < k; i++){ // 選擇 k 輪
            int cur = happiness[i] - i; // 考慮衰減，當前幸福值需減去 i
            if (cur < 0) break; // 如果幸福值小於 0，則不選擇
            ans += cur;
        }
        return ans;
    }
};
// @lc code=end

