/*
 * @lc app=leetcode id=2441 lang=cpp
 * @lcpr version=30122
 *
 * [2441] Largest Positive Integer That Exists With Its Negative
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int findMaxK(vector<int>& nums) {
        int ans = -1;
        unordered_set<int> visited;
        for (int x: nums) {
            if (visited.find(-x) != visited.end()) {
                ans = max(ans, abs(x));
            }
            visited.insert(x);
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [-1,2,-3,3]\n
// @lcpr case=end

// @lcpr case=start
// [-1,10,6,7,-7,1]\n
// @lcpr case=end

// @lcpr case=start
// [-10,8,6,7,-2,-3]\n
// @lcpr case=end

 */

