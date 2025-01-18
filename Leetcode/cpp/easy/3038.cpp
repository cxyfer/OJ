/*
 * @lc app=leetcode.cn id=3038 lang=cpp
 *
 * [3038] 相同分数的最大操作数目 I
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int maxOperations(vector<int>& nums) {
        // return solve1(nums);
        return solve2(nums);
    }
    int solve1(vector<int>& nums) {
        int n = nums.size();
        int ans = 1, target = nums[0] + nums[1];
        for (int i = 2; i < n; i += 2){
            if (i + 1 < n && nums[i] + nums[i+1] == target) ans++;
            else break;
        }
        return ans;
    }
    int solve2(vector<int>& nums) {
        int n = nums.size(), target = nums[0] + nums[1];
        for (int i = 3; i < n; i += 2){
            if (nums[i-1] + nums[i] != target) return i / 2;
        }
        return n / 2;
    }
};
// @lc code=end

