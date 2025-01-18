/*
 * @lc app=leetcode id=263 lang=cpp
 * @lcpr version=30112
 *
 * [263] Ugly Number
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    bool isUgly(int n) {
        vector<int> factors = {2, 3, 5};
        for (auto factor: factors){
            while (n > 0 && n % factor == 0){
                n /= factor;
            }
        }
        return (n == 1);
    }
};
// @lc code=end



/*
// @lcpr case=start
// 6\n
// @lcpr case=end

// @lcpr case=start
// 1\n
// @lcpr case=end

// @lcpr case=start
// 14\n
// @lcpr case=end

 */

