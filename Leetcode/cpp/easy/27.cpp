/*
 * @lc app=leetcode.cn id=27 lang=cpp
 *
 * [27] 移除元素
 */

// @lc code=start
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int n = nums.size();
        int i = 0, k = 0;
        while (i < n) {
            if (nums[i] != val) {
                nums[k++] = nums[i];
            }
            i++;
        }
        return k;
    }
};
// @lc code=end

