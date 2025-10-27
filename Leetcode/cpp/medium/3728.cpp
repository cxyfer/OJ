/*
 * @lc app=leetcode.cn id=3728 lang=cpp
 * @lcpr version=30204
 *
 * [3728] 边界与内部和相等的稳定子数组
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <ranges>

class Solution {
public:
    long long countStableSubarrays(vector<int>& capacity) {
        int n = capacity.size();
        long long ans = 0, s = 0;
        map<pair<long long, int>, int> cnt;
        for (auto [r, x] : views::enumerate(capacity)) {
            s += x;
            ans += cnt[{s - x - x, x}];
            if (r > 0) {
                int y = capacity[r - 1];
                cnt[{s - x, y}] += 1;
            }
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [9,3,3,3,9]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4,5]\n
// @lcpr case=end

// @lcpr case=start
// [-4,4,0,0,-8,-4]\n
// @lcpr case=end

 */

