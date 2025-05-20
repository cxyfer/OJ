/*
 * @lc app=leetcode.cn id=3355 lang=cpp
 * @lcpr version=30204
 *
 * [3355] 零数组变换 I
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    bool isZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        vector<int> diff(n + 1);
        for (auto& q : queries) {
            diff[q[0]]++;
            diff[q[1] + 1]--;
        }
        for (int i = 0; i < n; i++) {
            if (diff[i] < nums[i])
                return false;
            diff[i + 1] += diff[i];
        }
        return true;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,0,1]\n[[0,2]]\n
// @lcpr case=end

// @lcpr case=start
// [4,3,2,1]\n[[1,3],[0,2]]\n
// @lcpr case=end

 */

