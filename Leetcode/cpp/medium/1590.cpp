/*
 * @lc app=leetcode.cn id=1590 lang=cpp
 *
 * [1590] 使数组和能被 P 整除
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int minSubarray(vector<int>& nums, int p) {
        int n = nums.size();
        int r = 0;
        for (int x : nums) r = (r + x) % p;
        if (r == 0) return 0;
        unordered_map<int, int> pos;
        pos[0] = -1;
        int ans = n;
        int s = 0; // prefix sum
        for (int i = 0; i < n; ++i) {
            s = (s + nums[i]) % p;
            if (pos.find((s - r + p) % p) != pos.end()) {
                ans = min(ans, i - pos[(s - r + p) % p]);
            }
            pos[s] = i;
        }
        return ans < n ? ans : -1;
    }
};
// @lc code=end

