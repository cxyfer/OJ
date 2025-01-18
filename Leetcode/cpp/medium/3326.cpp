/*
 * @lc app=leetcode.cn id=3326 lang=cpp
 *
 * [3326] 使数组非递减的最少除法操作次数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
const int MAX = 1e6 + 5;
int LPF[MAX];

auto init = [] {
    for (int i = 2; i < MAX; i++) {
        if (LPF[i] == 0) {
            for (int j = i; j < MAX; j += i) {
                if (LPF[j] == 0) {
                    LPF[j] = i;
                }
            }
        }
    }
    return 0;
}();

class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n = nums.size();
        int ans = 0;
        for (int i = n - 2; i >= 0; i--) {
            if (nums[i] > nums[i + 1]) {
                nums[i] = LPF[nums[i]];
                if (nums[i] > nums[i + 1]) {
                    return -1;
                }
                ans++;
            }
        }
        return ans;
    }
};
// @lc code=end

