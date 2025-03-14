/*
 * @lc app=leetcode id=2226 lang=cpp
 *
 * [2226] Maximum Candies Allocated to K Children
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int maximumCandies(vector<int>& candies, long long k) {
        auto check = [&](auto &&dfs, int m) -> bool {
            long long tot = 0;
            for (auto&c : candies) tot += c / m;
            return tot >= k;
        };
        int left = 1, right = *max_element(candies.begin(), candies.end());
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (check(check, mid)) left = mid + 1;
            else right = mid - 1;
        }
        return right;
    }
};
// @lc code=end

