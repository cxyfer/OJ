/*
 * @lc app=leetcode.cn id=532 lang=cpp
 * @lcpr version=30204
 *
 * [532] 数组中的 k-diff 数对
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        unordered_map<int, int> cnt;
        for (int x : nums) cnt[x]++;
        return accumulate(cnt.begin(), cnt.end(), 0, [&](int ans, auto &p) {
            return ans + ((k > 0 && cnt.count(p.first + k)) || (k == 0 && p.second > 1));
        });
    }
};
// @lc code=end



/*
// @lcpr case=start
// [3, 1, 4, 1, 5]\n2\n
// @lcpr case=end

// @lcpr case=start
// [1, 2, 3, 4, 5]\n1\n
// @lcpr case=end

// @lcpr case=start
// [1, 3, 1, 5, 4]\n0\n
// @lcpr case=end

 */

