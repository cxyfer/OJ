/*
 * @lc app=leetcode.cn id=26 lang=cpp
 *
 * [26] 删除有序数组中的重复项
 */

// @lc code=start
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size();
        int i = 0, k = 0, j;
        while (i < n) {
            j = i;
            while (i < n && nums[i] == nums[j]) i++;
            nums[k++] = nums[j];
        }
        return k;
    }
};
// @lc code=end

