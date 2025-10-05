/*
 * @lc app=leetcode.cn id=11 lang=cpp
 * @lcpr version=30204
 *
 * [11] 盛最多水的容器
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int maxArea(vector<int>& height) {
        int n = height.size();
        int ans = 0;
        for (int left = 0, right = n - 1; left < right;) {
            int h = min(height[left], height[right]);
            ans = max(ans, h * (right - left));
            if (height[left] <= height[right])
                while (left < right and height[left] <= h) left++;
            else
                while (left < right and height[right] <= h) right--;
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,8,6,2,5,4,8,3,7]\n
// @lcpr case=end

// @lcpr case=start
// [1,1]\n
// @lcpr case=end

 */

