/*
 * @lc app=leetcode.cn id=2962 lang=cpp
 *
 * [2962] 统计最大元素出现至少 K 次的子数组
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    long long countSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        int mx = *max_element(nums.begin(), nums.end());
        int left = 0, cnt = 0;
        long long ans = 0;
        vector<int> pre(n + 1);
        for (int i = 0; i < n; i++) pre[i + 1] = pre[i] + (nums[i] == mx);
        for (int i = 0; i < n; i++) {
            int j = lower_bound(pre.begin(), pre.end(), pre[i] + k) - pre.begin();
            ans += n - (j - 1);
        }
        return ans;
    }
};

class Solution2 {
public:
    long long countSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        int mx = *max_element(nums.begin(), nums.end());
        int left = 0, cnt = 0;
        long long ans = 0;
        for (int right = 0; right < n; right++) {
            if (nums[right] == mx) cnt++;
            while (cnt == k)
                cnt -= nums[left++] == mx;
            ans += left;
        }
        return ans;
    }
};

// class Solution : public Solution1 {};
class Solution : public Solution2 {};
// @lc code=end

