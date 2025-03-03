/*
 * @lc app=leetcode id=2161 lang=cpp
 *
 * [2161] Partition Array According to Given Pivot
 */

// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        vector<int> p1, p2, p3;
        for (auto& x : nums) {
            if (x < pivot)
                p1.push_back(x);
            else if (x == pivot)
                p2.push_back(x);
            else
                p3.push_back(x);
        }
        p1.insert(p1.end(), p2.begin(), p2.end());
        p1.insert(p1.end(), p3.begin(), p3.end());
        return p1;
    }
};

class Solution2 {
   public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        int n = nums.size();
        vector<int> ans(n, pivot);
        int l = 0, r = n - 1;
        for (auto& x : nums) {
            if (x < pivot)
                ans[l++] = x;
            else if (x > pivot)
                ans[r--] = x;
        }
        reverse(ans.begin() + r + 1, ans.end());
        return ans;
    }
};

class Solution3 {
   public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        int n = nums.size();
        vector<int> ans(n, pivot);
        int l = 0, r = n - 1;
        for (int i = 0, j = n - 1; i < n && j >= 0; i++, j--) {
            if (nums[i] < pivot) ans[l++] = nums[i];
            if (nums[j] > pivot) ans[r--] = nums[j];
        }
        return ans;
    }
};

// class Solution : public Solution1 {};
// class Solution : public Solution2 {};
class Solution : public Solution3 {};
// @lc code=end
