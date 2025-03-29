/*
 * @lc app=leetcode.cn id=2818 lang=cpp
 * @lcpr version=30204
 *
 * [2818] 操作使得分最大
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
using LL = long long;
const LL MOD = 1e9 + 7;
const int MAXN = 1e5 + 10;

vector<int> scores(MAXN, 0);
auto init = []() {
    for (int i = 2; i < MAXN; i++)
        if (scores[i] == 0)
            for (int j = i; j < MAXN; j += i)
                scores[j]++;
    return 0;
}();

LL pow(LL x, int n, LL mod) {
    LL res = 1;
    while (n) {
        if (n & 1) res = res * x % mod;
        x = x * x % mod;
        n >>= 1;
    }
    return res;
}

class Solution {
public:
    int maximumScore(vector<int> &nums, int k) {
        int n = nums.size();
        vector<int> pre(n, -1), suf(n, n);
        stack<int> st;
        st.push(-1);
        for (int i = 0; i < n; i++) {
            while (st.top() != -1 && scores[nums[st.top()]] < scores[nums[i]]) {
                suf[st.top()] = i;
                st.pop();
            }
            pre[i] = st.top();
            st.push(i);
        }

        vector<int> idxs(n);
        iota(idxs.begin(), idxs.end(), 0);
        sort(idxs.begin(), idxs.end(), [&](const int i, const int j) {
            return nums[i] > nums[j];
        });

        LL ans = 1;
        for (int i: idxs) {
            LL v = min((LL) (i - pre[i]) * (suf[i] - i), (LL) k);
            ans = ans * pow(nums[i], v, MOD) % MOD;
            k -= v;
            if (k <= 0) break;
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [8,3,9,3,8]\n2\n
// @lcpr case=end

// @lcpr case=start
// [19,12,14,6,10,18]\n3\n
// @lcpr case=end

 */

