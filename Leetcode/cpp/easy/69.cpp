/*
 * @lc app=leetcode id=69 lang=cpp
 *
 * [69] Sqrt(x)
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
using i64 = long long;

class Solution {
public:
    int mySqrt(int x) {
        int left = 0, right = x;
        while (left <= right) {
            i64 mid = left + (right - left) / 2;
            if (mid * mid <= x)
                left = mid + 1;
            else
                right = mid - 1;
        }
        return right;
    }
};
// @lc code=end

