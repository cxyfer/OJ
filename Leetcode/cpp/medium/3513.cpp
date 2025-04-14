/*
 * @lc app=leetcode.cn id=3513 lang=cpp
 * @lcpr version=30204
 *
 * [3513] 不同 XOR 三元组的数目 I
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int uniqueXorTriplets(vector<int>& nums) {
        int n = nums.size();
        return n < 3 ? n : 1 << (32 - __builtin_clz(n));
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,2]\n
// @lcpr case=end

// @lcpr case=start
// [3,1,2]\n
// @lcpr case=end

 */

