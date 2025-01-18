/*
 * @lc app=leetcode.cn id=2903 lang=cpp
 *
 * [2903] 找出满足差值条件的下标 I
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<int> findIndices(vector<int>& nums, int indexDifference, int valueDifference) {
        // return solve1(nums, indexDifference, valueDifference);
        return solve2(nums, indexDifference, valueDifference);
    }
    vector<int> solve1(vector<int>& nums, int indexDifference, int valueDifference) {
        int n = nums.size();
        for (int i = 0; i < n; i++)
            for (int j = i + indexDifference; j < n; j++) // j - i >= indexDifference
                if (abs(nums[j] - nums[i]) >= valueDifference) 
                    return {i, j};
        return {-1, -1};
    }
    vector<int> solve2(vector<int>& nums, int indexDifference, int valueDifference) {
        int n = nums.size(), max_idx = 0, min_idx = 0;
        for (int j = indexDifference; j < n; j++){ // 枚舉右指針
            int i = j - indexDifference; // 左指針，與右指針相差 indexDifference
            // 更新 max_idx, min_idx
            if (nums[i] > nums[max_idx]) max_idx = i;
            else if (nums[i] < nums[min_idx]) min_idx = i;
            // 檢查是否存在答案
            if (nums[max_idx] - nums[j] >= valueDifference) return {max_idx, j};
            else if (nums[j] - nums[min_idx] >= valueDifference) return {min_idx, j};
        }
        return {-1, -1};
    }
};
// @lc code=end

