/*
 * @lc app=leetcode id=3162 lang=cpp
 *
 * [3162] Find the Number of Good Pairs I
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int numberOfPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        int m = nums1.size(), n = nums2.size();
        int ans = 0;
        for (int i = 0; i < m; i++) {
            if (nums1[i] % k != 0) continue;
            for (int j = 0; j < n; j++) {
                if (nums1[i] % (nums2[j] * k) == 0) {
                    ans++;
                }
            }
        }
        return ans;
    }
};
// @lc code=end

