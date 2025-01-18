/*
 * @lc app=leetcode id=2966 lang=cpp
 * @lcpr version=30112
 *
 * [2966] Divide Array Into Arrays With Max Difference
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<vector<int>> divideArray(vector<int>& nums, int k) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;
        for (int i=0; i<n; i+=3){
            if (nums[i+2] - nums[i] > k){
                return {};
            }
            ans.push_back({nums[i], nums[i+1], nums[i+2]});
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,3,4,8,7,9,3,5,1]\n2\n
// @lcpr case=end

// @lcpr case=start
// [1,3,3,2,7,3]\n3\n
// @lcpr case=end

 */

