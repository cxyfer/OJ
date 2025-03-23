/*
 * @lc app=leetcode.cn id=15 lang=cpp
 * @lcpr version=30204
 *
 * [15] 三数之和
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
/*
 * 基础算法精讲 01 - Two pointers
 * 
 * Extend from 167. Sum of Two Numbers II - Input Ordered Array
 * i < left < right < n
 * 
 * 一些優化：
 * 1. 如果 nums[i] > 0，後面的數字都會大於 0，不可能有三個數字相加等於 0，可以終止迴圈
 * 2. 如果 nums[i] + nums[i+1] + nums[i+2] > 0，則後面任三個數字相加都會大於 0，不可能有三個數字相加等於 0，可以終止迴圈
 * 3. 如果 nums[i] + nums[n-2] + nums[n-1] < 0，則可以跳過 nums[i] ，因為 nums[i] + nums[left] + nums[right] 只會更小
 *    - 注意這種情況下，枚舉 i 後面的數字仍然有可能有答案，故只需要跳過 i 即可
 * 
 * TS: O(n log n + n^2) = O(n^2)
 * SC: O(1), ignore the space of sorting
*/
// @lc code=start
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int n = nums.size();
        if (n < 3) return {};
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;
        // i < left < right < n
        for (int i = 0; i < n - 2; i++) {
            if (i > 0 && nums[i] == nums[i-1]) continue; // 跳過重複的答案
            if (nums[i] > 0) break; // 1.
            if (nums[i] + nums[i+1] + nums[i+2] > 0) break; // 2.
            if (nums[i] + nums[n-2] + nums[n-1] < 0) continue; // 3.
            int left = i + 1, right = n - 1;
            while (left < right) {
                int s = nums[i] + nums[left] + nums[right];
                if (s < 0) left++; // 太小了，左邊的數字太小，往右移
                else if (s > 0) right--; // 太大了，右邊的數字太大，往左移
                else {
                    ans.push_back({nums[i], nums[left], nums[right]});
                    // 跳過重複的答案
                    while (left < right && nums[left] == nums[left+1]) left++;
                    while (left < right && nums[right] == nums[right-1]) right--;
                    // 找下一個答案
                    left++;
                    right--;
                }
            }
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [-1,0,1,2,-1,-4]\n
// @lcpr case=end

// @lcpr case=start
// [0,1,1]\n
// @lcpr case=end

// @lcpr case=start
// [0,0,0]\n
// @lcpr case=end

 */

