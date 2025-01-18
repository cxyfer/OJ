/*
 * @lc app=leetcode.cn id=1482 lang=cpp
 *
 * [1482] 制作 m 束花所需的最少天数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int minDays(vector<int>& bloomDay, int m, int k) {
        
        // check if we can make m bouquets with k flowers in d days
        auto check = [&](int d) {
            int res = 0, cur = 0;
            for (int bloom : bloomDay) {
                if (bloom <= d) {
                    cur++;
                    if (cur == k) {
                        res++;
                        cur = 0;
                    }
                } else {  // not adjacent
                    cur = 0;
                }
            }
            return res >= m;
        };

        int mx = INT_MIN, mn = INT_MAX;
        for (int bloom : bloomDay) {
            mx = max(mx, bloom);
            mn = min(mn, bloom);
        }
        int left = mn, right = mx;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (check(mid)) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return left <= mx ? left : -1;
    }
};
// @lc code=end