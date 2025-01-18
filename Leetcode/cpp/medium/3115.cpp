/*
 * @lc app=leetcode.cn id=3115 lang=cpp
 *
 * [3115] 质数的最大距离
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
const int N = 105;

bool is_prime[N];
auto init = []() {
    memset(is_prime, true, sizeof(is_prime));
    is_prime[0] = is_prime[1] = false;
    for (int i = 2; i * i < N; i++) {
        if (is_prime[i]) {
            for (int j = i * i; j < N; j += i) {
                is_prime[j] = false;
            }
        }
    }
    return 0;
}();

class Solution {
public:
    int maximumPrimeDifference(vector<int>& nums) {
        int i = 0, j = nums.size() - 1;
        while (!is_prime[nums[i]]) i++;
        while (!is_prime[nums[j]]) j--;
        return j - i;
    }
};
// @lc code=end

