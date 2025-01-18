/*
 * @lc app=leetcode id=258 lang=cpp
 * @lcpr version=30112
 *
 * [258] Add Digits
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int addDigits(int num) {
        int sod = 0; // sum of digits
        while (num >= 10){
            sod = 0;
            while (num > 0){
                sod += num % 10;
                num /= 10;
            }
            num = sod;
        }
        return num;
    }
};
// @lc code=end



/*
// @lcpr case=start
// 38\n
// @lcpr case=end

// @lcpr case=start
// 0\n
// @lcpr case=end

 */

