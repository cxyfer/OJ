/*
 * @lc app=leetcode.cn id=1248 lang=cpp
 *
 * [1248] 统计「优美子数组」
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> s(n + 1);
        for (int i = 0; i < n; i++)
            s[i + 1] = s[i] + nums[i] % 2;
        int ans = 0;
        for (int i = 0; i < n; i++) {
            ans += upper_bound(s.begin(), s.end(), s[i] + k) - lower_bound(s.begin(), s.end(), s[i] + k);
        }
        return ans;
    }
};

class Solution2 {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int n = nums.size(), ans = 0, s = 0;
        vector<int> cnt(n + 1);
        cnt[0] = 1;
        for (int x : nums) {
            s += x & 1;
            if (s >= k) ans += cnt[s - k];
            cnt[s]++;
        }
        return ans;
    }
};

class Solution3 {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int n = nums.size(), ans = 0;
        vector<int> odd;
        odd.push_back(-1); // dummy
        for (int i = 0; i < n; i++)
            if (nums[i] & 1) odd.push_back(i);
        odd.push_back(n); // dummy
        for (int i = 1; i + k < odd.size(); i++) {
            int j = i + k - 1;
            ans += (odd[i] - odd[i - 1]) * (odd[j + 1] - odd[j]);
        }
        return ans;
    }
};

// class Solution : public Solution1 {};
// class Solution : public Solution2 {};
class Solution : public Solution3 {};
// @lc code=end

