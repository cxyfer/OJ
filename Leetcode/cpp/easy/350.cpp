/*
 * @lc app=leetcode.cn id=350 lang=cpp
 *
 * [350] 两个数组的交集 II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        vector<int> cnt1(1001), cnt2(1001);
        for (int x : nums1) cnt1[x]++;
        for (int x : nums2) cnt2[x]++;
        vector<int> ans;
        for (int x = 0; x <= 1000; x++) {
            for (int i = 0; i < min(cnt1[x], cnt2[x]); i++) {
                ans.push_back(x);
            }
        }
        return ans;
    }
};

class Solution2 {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        // unordered_map<int, int> cnt;
        vector<int> cnt(1001);
        for (int x : nums1) cnt[x]++;
        vector<int> ans;
        for (int x : nums2) {
            if (cnt[x] > 0) {
                ans.push_back(x);
                cnt[x]--;
            }
        }
        return ans;
    }
};

class Solution3 {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());

        int m = nums1.size(), n = nums2.size();
        int i = 0, j = 0;
        vector<int> ans;
        while (i < m && j < n) {
            if (nums1[i] == nums2[j]) {
                ans.push_back(nums1[i]);
                i++, j++;
            } else if (nums1[i] < nums2[j]) {
                i++;
            } else {
                j++;
            }
        }
        return ans;
    }
};

// class Solution : public Solution1 {};
// class Solution : public Solution2 {};
class Solution : public Solution3 {};
// @lc code=end

