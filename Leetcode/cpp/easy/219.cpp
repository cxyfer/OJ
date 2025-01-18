/*
 * @lc app=leetcode id=219 lang=cpp
 * @lcpr version=30201
 *
 * [219] 存在重复元素 II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> last;
        for (int i = 0; i < nums.size(); i++) {
            if (last.count(nums[i]) && i - last[nums[i]] <= k) {
                return true;
            }
            last[nums[i]] = i;
        }
        return false;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,2,3,1]\n3\n
// @lcpr case=end

// @lcpr case=start
// [1,0,1,1]\n1\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,1,2,3]\n2\n
// @lcpr case=end

 */

