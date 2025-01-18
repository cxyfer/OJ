/*
 * @lc app=leetcode.cn id=2601 lang=cpp
 *
 * [2601] 质数减法运算
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
const int MAXN = 1000;
vector<int> primes;
bool is_prime[MAXN + 1];

int init = []() {
    memset(is_prime, true, sizeof(is_prime));
    is_prime[0] = is_prime[1] = false;
    for (int i = 2; i <= MAXN; ++i) {
        if (is_prime[i]) {
            primes.push_back(i);
            for (int j = i * i; j <= MAXN; j += i) {
                is_prime[j] = false;
            }
        }
    }
    return 0;
}();

class Solution {
public:
    bool primeSubOperation(vector<int>& nums) {
        int pre = 0;
        for (int x : nums) {
            if (x <= pre) return false;
            int idx = lower_bound(primes.begin(), primes.end(), x - pre) - primes.begin() - 1;
            pre = (idx >= 0 ? (x - primes[idx]) : x);
        }
        return true;
    }
};
// @lc code=end

int main() {
    Solution sol = Solution();
    vector<int> nums = {4, 9, 6, 10};
    if (sol.primeSubOperation(nums)) {
        cout << "true" << endl;
    } else {
        cout << "false" << endl;
    }
    return 0;
}