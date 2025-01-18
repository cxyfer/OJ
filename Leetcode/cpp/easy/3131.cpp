/*
 * @lc app=leetcode id=3131 lang=cpp
 * @lcpr version=30122
 *
 * [3131] Find the Integer Added to Array I
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int addedInteger(vector<int>& nums1, vector<int>& nums2) {
        int n=nums1.size(), mx1=-1, mx2=-1;
        for (int i=0; i<n; i++) {
            if (nums1[i] > mx1) mx1 = nums1[i];
            if (nums2[i] > mx2) mx2 = nums2[i];
        }
        return mx2 - mx1;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [2,6,4]\n[9,7,5]\n
// @lcpr case=end

// @lcpr case=start
// [10]\n[5]\n
// @lcpr case=end

// @lcpr case=start
// [1,1,1,1]\n[1,1,1,1]\n
// @lcpr case=end

 */

