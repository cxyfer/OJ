/*
 * @lc app=leetcode id=1512 lang=cpp
 * @lcpr version=30112
 *
 * [1512] Number of Good Pairs
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int ans = 0;
        map<int, int> cnt;
        for (auto num : nums) {
            ans += cnt[num];
            cnt[num]++;
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,2,3,1,1,3]\n
// @lcpr case=end

// @lcpr case=start
// [1,1,1,1]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3]\n
// @lcpr case=end

 */

