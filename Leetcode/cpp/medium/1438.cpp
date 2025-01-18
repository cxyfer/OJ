/*
 * @lc app=leetcode.cn id=1438 lang=cpp
 *
 * [1438] 绝对差不超过限制的最长连续子数组
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int longestSubarray(vector<int>& nums, int limit) {
        int n = nums.size();
        multiset<int> s;
        int ans = 0, left = 0;
        for (int right = 0; right < n; right++) {
            s.insert(nums[right]);
            while (*s.rbegin() - *s.begin() > limit) {
                s.erase(s.find(nums[left]));
                left++;
            }
            ans = max(ans, right - left + 1);
        }
        return ans;
    }
};

class Solution2 {
public:
    int longestSubarray(vector<int>& nums, int limit) {
        int n = nums.size();
        deque<int> q_min, q_max;
        int ans = 0, left = 0;
        for (int right = 0; right < n; right++) {
            while (!q_min.empty() && nums[right] < q_min.back())
                q_min.pop_back();
            while (!q_max.empty() && nums[right] > q_max.back())
                q_max.pop_back();
            q_min.push_back(nums[right]);
            q_max.push_back(nums[right]);
            while (q_max.front() - q_min.front() > limit) {
                if (nums[left] == q_min.front()) q_min.pop_front();
                if (nums[left] == q_max.front()) q_max.pop_front();
                left++;
            }
            ans = max(ans, right - left + 1);
        }
        return ans;
    }
};

// class Solution : public Solution1 {};
class Solution : public Solution2 {};
// @lc code=end