/*
 * @lc app=leetcode.cn id=2197 lang=cpp
 * @lcpr version=30204
 *
 * [2197] 替换数组中的非互质数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<int> replaceNonCoprimes(vector<int>& nums) {
        vector<int> st;
        for (int x : nums) {
            while (!st.empty() && gcd(st.back(), x) > 1) {
                int y = st.back();
                st.pop_back();
                x = 1LL * y * x / gcd(y, x);
            }
            st.push_back(x);
        }
        return st;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [6,4,3,2,7,6,2]\n
// @lcpr case=end

// @lcpr case=start
// [2,2,1,1,3,3,3]\n
// @lcpr case=end

 */

