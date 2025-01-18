/*
 * @lc app=leetcode.cn id=2595 lang=cpp
 *
 * [2595] 奇偶位数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    vector<int> evenOddBit(int n) {
        vector<int> ans(2, 0);
        int idx = 0;
        while (n) {
            ans[idx] += n & 1;
            idx ^= 1;
            n >>= 1;
        }
        return ans;
    }
};

class Solution2 {
public:
    vector<int> evenOddBit(int n) {
        int mask = 0xAAAAAAAA;
        return {__builtin_popcount(n & (mask >> 1)), __builtin_popcount(n & mask)};
    }
};

class Solution : public Solution1 {};
// class Solution : public Solution2 {};
// @lc code=end

