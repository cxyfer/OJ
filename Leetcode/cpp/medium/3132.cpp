/*
 * @lc app=leetcode id=3132 lang=cpp
 * @lcpr version=30122
 *
 * [3132] Find the Integer Added to Array II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start

    // def solve1(self, nums1: List[int], nums2: List[int]) -> int:
    //     cnt1, cnt2 = Counter(nums1), Counter(nums2)
    //     k1 = sorted(cnt1.keys())
    //     mx2 = max(cnt2.keys())

    //     def check(x): # 若差是 x ，其「缺失」的數字數量
    //         res = 0
    //         for k, v in cnt1.items():
    //             if k + x not in cnt2: # 全部缺失
    //                 res += v
    //             elif cnt2[k + x] < v: # 部分缺失
    //                 res += v - cnt2[k + x]
    //         return res
        
    //     for i in range(3): # 0, 1, 2
    //         mx1 = k1[-1-i] # -1, -2, -3 ，nums1 中最大的數是 mx1 ，則根據題意只有三種可能
    //         x = mx2 - mx1
    //         if check(x) == 2-i: # 缺失的數字數量依次必須是 2, 1, 0
    //             return x
    //         cnt1[mx1] -= 1
    //         if cnt1[mx1] == 0:
    //             del cnt1[mx1]
    //     return -1

class Solution {
public:
    int minimumAddedInteger(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size(), m = nums2.size();
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        for (int k = 2; k >= 0; k--) {
            int x = nums2[0] - nums1[k];
            int i = 0, j = 0;
            while (i < n && j < m) {
                if (nums1[i] + x == nums2[j]) {
                    j++;
                }
                i++;
            }
            if (j == m) {
                return x;
            }
        }
        return -1;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [4,20,16,12,8]\n[14,18,10]\n
// @lcpr case=end

// @lcpr case=start
// [3,5,5,3]\n[7,7]\n
// @lcpr case=end

 */

