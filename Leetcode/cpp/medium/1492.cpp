/*
 * @lc app=leetcode.cn id=1492 lang=cpp
 *
 * [1492] n 的第 k 个因子
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    /*
        1. Brute force
            - Time: O(n)
            - Space: O(n) / O(1)
        2. Optimized brute force
            - Time: O(sqrt(n))
            - Space: O(sqrt(n)) / O(1)
    */
    int kthFactor(int n, int k) {
        // return solve1a(n, k);
        // return solve1b(n, k);
        // return solve2a(n, k);
        return solve2b(n, k);
    }
    int solve1a(int n, int k) {
        vector<int> factors;
        for (int i = 1; i <= n; i++) {
            if (n % i == 0) factors.push_back(i);
        }
        return k <= factors.size() ? factors[k-1] : -1;
    }
    int solve1b(int n, int k) {
        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                if (--k == 0) return i;
            }
        }
        return -1;
    }
    int solve2a(int n, int k) {
        vector<int> factors;
        for (int i = 1; i * i <= n; i++) {
            if (n % i == 0) factors.push_back(i);
        }
        int m = factors.size();
        if (factors[m-1] * factors[m-1] == n) m--;
        for (int i = m-1; i >= 0; i--) {
            factors.push_back(n / factors[i]);
        }
        return k <= factors.size() ? factors[k-1] : -1;
    }
    int solve2b(int n, int k) {
        int i;
        for (i = 1; i * i <= n; i++) { // 正序遍歷到 sqrt(n)
            if (n % i == 0) {
                if (--k == 0) return i;
            }
        }
        i--; // 最後的 i 會使 i * i > n
        if (i * i == n) i--;
        for (int j = i; j > 0; j--) { // 逆序遍歷
            if (n % j == 0) {
                if (--k == 0) return n / j;
            }
        }
        return -1;
    }
};
// @lc code=end

