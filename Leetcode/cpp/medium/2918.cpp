/*
 * @lc app=leetcode.cn id=2918 lang=cpp
 * @lcpr version=30204
 *
 * [2918] 数组的最小相等和
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    long long minSum(vector<int>& nums1, vector<int>& nums2) {
        int cnt1 = count(nums1.begin(), nums1.end(), 0);
        int cnt2 = count(nums2.begin(), nums2.end(), 0);
        long long s1 = accumulate(nums1.begin(), nums1.end(), 0LL) + cnt1;
        long long s2 = accumulate(nums2.begin(), nums2.end(), 0LL) + cnt2;
        if (s1 < s2 && cnt1 == 0 || s2 < s1 && cnt2 == 0)
            return -1;
        return max(s1, s2);
    }
};
// @lc code=end



/*
// @lcpr case=start
// [3,2,0,1,0]\n[6,5,0]\n
// @lcpr case=end

// @lcpr case=start
// [2,0,2,0]\n[1,4]\n
// @lcpr case=end

 */

