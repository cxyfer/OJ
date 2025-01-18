/*
 * @lc app=leetcode.cn id=2761 lang=cpp
 *
 * [2761] 和等于目标值的质数对
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
using LL = long long;
class Solution {
public:
    vector<vector<int>> findPrimePairs(int n) {
        vector<int> is_prime(max(2, n), true); // Sieve of Eratosthenes
        is_prime[0] = is_prime[1] = false;
        for (int i = 2; i * i < n; ++i){
            if (is_prime[i]){
                for (LL j = i * i; j < n; j += i){
                    is_prime[j] = false;
                }
            }
        }
        vector<vector<int>> ans;
        if (n >= 4 && is_prime[n - 2]) ans.push_back({2, n - 2});
        for (int i = 3; i <= n/2; i += 2){
            if (is_prime[i] && is_prime[n - i]){
                ans.push_back({i, n - i});
            }
        }
        return ans;
    }
};
// @lc code=end

int main() {
    Solution sol = Solution();
    auto ans = sol.findPrimePairs(1);
    for (auto &v : ans){
        for (int i : v){
            cout << i << " ";
        }
        cout << endl;
    }
    return 0;
}