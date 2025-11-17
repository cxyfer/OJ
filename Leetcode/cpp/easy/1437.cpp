/*
 * @lc app=leetcode.cn id=1437 lang=cpp
 * @lcpr version=30204
 *
 * [1437] 是否所有 1 都至少相隔 k 个元素
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    bool kLengthApart(vector<int>& nums, int k) {
        int n = nums.size();
        int last = -k - 1;
        for (int i = 0; i < n; i++) {
            if (nums[i] == 1) {
                if (i - last <= k)
                    return false;
                last = i;
            }
        }
        return true;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,0,0,0,1,0,0,1]\n2\n
// @lcpr case=end

// @lcpr case=start
// [1,0,0,1,0,1]\n2\n
// @lcpr case=end

 */

