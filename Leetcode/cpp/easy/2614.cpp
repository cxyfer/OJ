/*
 * @lc app=leetcode.cn id=2614 lang=cpp
 *
 * [2614] Prime In Diagonal
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start

const int MAXN = 4e6 + 5;
bool is_prime[MAXN];
auto init = []() {
    memset(is_prime, true, sizeof(is_prime));
    is_prime[0] = is_prime[1] = false;
    for (long long i = 2; i < MAXN; i++) {
        if (is_prime[i]) {
            for (long long j = i * i; j < MAXN; j += i)
                is_prime[j] = false;
        }
    }
    return 0;
}();

class Solution {
public:
    int diagonalPrime(vector<vector<int>>& nums) {
        int n = nums.size(), ans = 0;
        for (int i = 0; i < n; i++)
            for (int x : {nums[i][i], nums[i][n-1-i]})
                if (is_prime[x]) ans = max(ans, x);
        return ans;
    }
};
// @lc code=end