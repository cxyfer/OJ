/*
 * @lc app=leetcode.cn id=2461 lang=cpp
 *
 * [2461] 长度为 K 子数组中的最大和
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {
        int n = nums.size();
        int left = 0, have = 0;
        long long ans = 0, s = 0;
        unordered_map<int, int> cnt;
        for (int right = 0; right < n; ++right) {
            // 1. 入窗口
            int x = nums[right];
            cnt[x]++;
            s += x;
            if (cnt[x] == 1) have++;
            if (right < k - 1) continue;
            // 2. 更新答案
            if (have == k) ans = max(ans, s);
            // 3. 出窗口
            int y = nums[left++];
            cnt[y]--;
            s -= y;
            if (cnt[y] == 0) have--;
        }
        return ans;
    }
};
// @lc code=end

