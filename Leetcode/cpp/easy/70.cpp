/*
 * @lc app=leetcode.cn id=70 lang=cpp
 *
 * [70] 爬楼梯
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
using LL = long long;
class Solution {
public:
    /*
        1. Dynamic Programming
            O(n)
        2. Matrix Exponentiation
            O(logn)
        3. Fibonacci Formula
            O(1)
    */
    int climbStairs(int n) {
        // return solve1a(n);
        // return solve1b(n);
        return solve2(n);
        // return solve3(n);
    }
    int solve1a(int n) {
        vector<int> dp(n+1, 0);
        dp[0] = dp[1] = 1;
        for (int i=2; i<=n; i++){
            dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n];
    }
    int solve1b(int n) {
        int p = 0, q = 0, r = 1;
        for (int i=0; i<n; i++){
            p = q;
            q = r;
            r = p + q;
        }
        return r;
    }
    int solve2(int n) {
        vector<vector<LL>> matrix = {{1, 1}, {1, 0}};
        auto matrix_mul = [&](vector<vector<LL>>& a, vector<vector<LL>>& b) -> vector<vector<LL>> {
            int x = a.size(), y = b.size(), z = b[0].size();
            vector<vector<LL>> res(x, vector<LL>(z, 0));
            for (int i=0; i<x; i++){
                for (int j=0; j<z; j++){
                    LL c = 0;
                    for (int k=0; k<y; k++){
                        c += a[i][k] * b[k][j];
                    }
                    res[i][j] = c;
                }
            }
            return res;
        };
        auto matrix_pow = [&](vector<vector<LL>>& m, int n) -> vector<vector<LL>> {
            vector<vector<LL>> res = {{1, 0}, {0, 1}};
            while (n){
                if (n & 1){
                    res = matrix_mul(res, m);
                }
                m = matrix_mul(m, m);
                n >>= 1;
            }
            return res;
        };
        return matrix_pow(matrix, n)[0][0];
    }
    int solve3(int n) {
        double sqrt5 = sqrt(5);
        double fibn = pow((1 + sqrt5) / 2, n+1) - pow((1 - sqrt5) / 2, n+1);
        return (int)(fibn / sqrt5);
    }
};
// @lc code=end

