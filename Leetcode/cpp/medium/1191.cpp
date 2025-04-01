/*
 * @lc app=leetcode.cn id=1191 lang=cpp
 * @lcpr version=30204
 *
 * [1191] K 次串联后最大子数组之和
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
    const int MOD = 1e9 + 7;
public:
    int kConcatenationMaxSum(vector<int>& arr, int k) {
        int n = arr.size();
        int s = accumulate(arr.begin(), arr.end(), 0);
        vector<int> A(arr.begin(), arr.end());
        if (k > 1) A.insert(A.end(), arr.begin(), arr.end());
        int ans = 0, f = 0;
        for (int x : A) {
            f = max(x, f + x);
            ans = max(ans, f);
        }
        if (s > 0 && k > 1) while (k-- > 2) ans = (ans + s) % MOD;
        return ans % MOD;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,2]\n3\n
// @lcpr case=end

// @lcpr case=start
// [1,-2,1]\n5\n
// @lcpr case=end

// @lcpr case=start
// [-1,-2]\n7\n
// @lcpr case=end

 */

