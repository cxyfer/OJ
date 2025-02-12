/*
 * @lc app=leetcode.cn id=1760 lang=cpp
 *
 * [1760] 袋子里最少数目的球
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int minimumSize(vector<int>& nums, int maxOperations) {
        auto check = [&](int k) -> bool {
            int cnt = 0;
            for (int x : nums)
                cnt += (x - 1) / k;
            return cnt <= maxOperations;
        };
        int left = 1, right = *max_element(nums.begin(), nums.end());
        while (left <= right) {
            int mid = (left + right) / 2;
            if (check(mid)) right = mid - 1;
            else left = mid + 1;
        }
        return left;
    }
};
// @lc code=end

