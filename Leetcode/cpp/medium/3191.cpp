/*
 * @lc app=leetcode id=3191 lang=cpp
 *
 * [3191] Minimum Operations to Make Binary Array Elements Equal to One I
 */

// @lc code=start
class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n = nums.size(), ans = 0;
        for (int i = 0; i < n - 2; i++) {
            if (nums[i] == 0) {
                nums[i] = 1;
                nums[i + 1] ^= 1;
                nums[i + 2] ^= 1;
                ans++;
            }
        }
        for (int i = n - 2; i < n; i++)
            if (nums[i] == 0)
                return -1;
        return ans;
    }
};
// @lc code=end

