/*
 * @lc app=leetcode.cn id=3495 lang=cpp
 * @lcpr version=30204
 *
 * [3495] 使数组元素都变为零的最少操作次数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
using LL = long long;
const int E = 15;

vector<LL> p(E, 1), s(E);
auto init = []() {
    for (int i = 1; i < E; ++i) p[i] = p[i - 1] * 4;
    for (int i = 1; i < E; ++i) s[i] = s[i - 1] + (p[i] - p[i - 1]) * i;
    return 0;
}();

LL f(LL x) {
    if (x == 0) return 0;
    int idx = upper_bound(p.begin(), p.end(), x) - p.begin();
    return s[idx - 1] + (x - p[idx - 1] + 1) * idx;
}

class Solution {
public:
    long long minOperations(vector<vector<int>>& queries) {
        LL ans = 0;
        for (auto& q : queries) {
            int l = q[0], r = q[1];
            ans += (f(r) - f(l - 1) + 1) / 2;
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [[1,2],[2,4]]\n
// @lcpr case=end

// @lcpr case=start
// [[2,6]]\n
// @lcpr case=end

 */

