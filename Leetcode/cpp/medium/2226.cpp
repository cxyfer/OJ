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
        long long tot = accumulate(candies.begin(), candies.end(), 0LL);
        if (tot < k) return 0;

        auto check = [&](auto &&dfs, int m) -> bool {
            long long res = 0;
            for (auto&c : candies) {
                res += c / m;
            }
            return res >= k;
        };
        
        int left = 1, right = (int) (tot / k);
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (check(check, mid)) left = mid + 1;
            else right = mid - 1;
        }
        return right;
    }
};
// @lc code=end

