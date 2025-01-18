/*
 * @lc app=leetcode.cn id=2614 lang=cpp
 *
 * [2614] 对角线上的质数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int diagonalPrime(vector<vector<int>>& nums) {
        auto is_prime = [](int n) {
            if (n < 2 || n % 2 == 0 && n != 2) return false;
            for (int i = 3; i <= sqrt(n); i += 2) {
                if (n % i == 0) return false;
            }
            return true;
        };
        int n = nums.size(), ans = 0;
        for (int i = 0; i < n; i++) {
            for (int x : {nums[i][i], nums[i][n-1-i]}) {
                if (x > ans && is_prime(x)) ans = x; // 先判斷是否比 ans 大，再判斷是否是質數
            }
        }
        return ans;
    }
};
// @lc code=end

