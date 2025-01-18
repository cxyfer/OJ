/*
 * @lc app=leetcode.cn id=2905 lang=cpp
 *
 * [2905] 找出满足差值条件的下标 II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<int> findIndices(vector<int>& nums, int indexDifference, int valueDifference) {
        int n = nums.size(), max_idx = 0, min_idx = 0;
        for (int j = indexDifference; j < n; j++){
            int i = j - indexDifference;
            // 更新
            if (nums[i] > nums[max_idx]) max_idx = i;
            else if (nums[i] < nums[min_idx]) min_idx = i;
            // 檢查是否有答案
            if (nums[max_idx] - nums[j] >= valueDifference) return {max_idx, j};
            else if (nums[j] - nums[min_idx] >= valueDifference) return {min_idx, j};
        }
        return {-1, -1};
    }
};
// @lc code=end

int main() {
  cout << "Hello World!";
}