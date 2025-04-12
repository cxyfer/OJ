/*
 * @lc app=leetcode.cn id=3272 lang=cpp
 * @lcpr version=30204
 *
 * [3272] 统计好整数的数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
vector<long long> fact(11);
auto init = []() {
    fact[0] = 1;
    for (int i = 1; i < 11; i++) fact[i] = fact[i - 1] * i;
    return 0;
}();

class Solution {
public:
    long long countGoodIntegers(int n, int k) {
        unordered_set<string> vis;
        long long base = pow(10, (n - 1) / 2);
        for (long long i = base; i < base * 10; i++) {
            string s = to_string(i);
            s += string(s.rbegin() + (n & 1), s.rend());
            if (stoll(s) % k) continue;
            sort(s.begin(), s.end());
            vis.insert(s);
        }
        long long ans = 0;
        for (auto s : vis) {
            vector<int> cnt(10);
            for (auto ch : s) cnt[ch - '0']++;
            long long cur = (n - cnt[0]) * fact[n - 1];
            for (auto x : cnt) cur /= fact[x];
            ans += cur;
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// 3\n5\n
// @lcpr case=end

// @lcpr case=start
// 1\n4\n
// @lcpr case=end

// @lcpr case=start
// 5\n6\n
// @lcpr case=end

 */

