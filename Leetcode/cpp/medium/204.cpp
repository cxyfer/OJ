/*
 * @lc app=leetcode.cn id=204 lang=cpp
 *
 * [204] 计数质数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
using LL = long long;
class Solution {
public:
    int countPrimes(int n) {
        vector<int> is_prime(n, true);
        for (int i = 2; i * i < n; ++i){
            if (is_prime[i]){
                for (LL j = i * i; j < n; j += i){
                    is_prime[j] = false;
                }
            }
        }
        int ans = 0;
        for (int i = 2; i < n; ++i){
            if (is_prime[i]) ans++;
        }
        return ans;
    }
};
// @lc code=end

