/*
 * @lc app=leetcode.cn id=321 lang=cpp
 *
 * [321] 拼接最大数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    /*
        Similar to 402. Remove K Digits
        將問題轉換成從兩個陣列中分別選擇最大的 k1 和 k2 個數字，再合併成最大的數字
    */
    vector<int> maxNumber(vector<int>& nums1, vector<int>& nums2, int k) {
        vector<int> ans;
        int m = nums1.size(), n = nums2.size();
        for (int k1 = 0; k1 <= k; k1++) {
            int k2 = k - k1;
            if (k1 > m || k2 > n) continue;
            vector<int> mx1 = pick(nums1, k1), mx2 = pick(nums2, k2);
            vector<int> cur;
            while (!mx1.empty() || !mx2.empty()) {
                if (mx1 > mx2) {
                    cur.push_back(mx1[0]);
                    mx1.erase(mx1.begin());
                } else {
                    cur.push_back(mx2[0]);
                    mx2.erase(mx2.begin());
                }
            }
            ans = max(ans, cur);
        }
        return ans;
    }
    vector<int> pick(vector<int>& nums, int k) {
        vector<int> st;
        int d = nums.size() - k;
        for (int x : nums) {
            while (d && !st.empty() && st.back() < x) {
                st.pop_back();
                d--;
            }
            st.push_back(x);
        }
        return vector<int>(st.begin(), st.begin() + k);
    }
};
// @lc code=end

