/*
 * @lc app=leetcode id=2570 lang=cpp
 *
 * [2570] Merge Two 2D Arrays by Summing Values
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<vector<int>> mergeArrays(vector<vector<int>>& nums1, vector<vector<int>>& nums2) {
        int n = nums1.size(), m = nums2.size();
        int i = 0, j = 0;
        vector<vector<int>> ans;
        while (i < n || j < m) {
            if (j == m || (i < n && nums1[i][0] < nums2[j][0]))
                ans.push_back({nums1[i][0], nums1[i++][1]});
            else if (i == n || (j < m && nums1[i][0] > nums2[j][0]))
                ans.push_back({nums2[j][0], nums2[j++][1]});
            else
                ans.push_back({nums1[i][0], nums1[i++][1] + nums2[j++][1]});
        }
        return ans;
    }
};
// @lc code=end

