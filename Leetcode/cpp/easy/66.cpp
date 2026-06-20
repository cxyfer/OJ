/*
 * @lc app=leetcode.cn id=66 lang=cpp
 * @lcpr version=30204
 *
 * [66] 加一
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size();
        digits[n - 1] += 1;
        int i = n - 1;
        while (i >= 0) {
            if (digits[i] < 10) {
                break;
            }
            digits[i] -= 10;
            if (i == 0) {
                digits.insert(digits.begin(), 1);
                break;
            }
            digits[i - 1] += 1;
            i -= 1;
        }
        return digits;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,2,3]\n
// @lcpr case=end

// @lcpr case=start
// [4,3,2,1]\n
// @lcpr case=end

// @lcpr case=start
// [9]\n
// @lcpr case=end

 */

