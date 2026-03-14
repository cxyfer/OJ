/*
 * @lc app=leetcode id=1009 lang=cpp
 *
 * [1009] Complement of Base 10 Integer
 */


// @lcpr-template-start
#include <bits/stdc++.h>
#include <bit>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int bitwiseComplement(int n) {
        return n ^ ((1 << (bit_width(static_cast<unsigned>(max(n, 1))))) - 1);
    }
};
// @lc code=end

