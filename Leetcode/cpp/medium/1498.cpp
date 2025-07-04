/*
 * @lc app=leetcode.cn id=1498 lang=cpp
 * @lcpr version=30204
 *
 * [1498] 满足条件的子序列数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <ranges>
using ll = long long;
const int MOD = 1e9 + 7;

ll pow(ll a, ll b, ll m) {
    ll res = 1;
    while (b) {
        if (b & 1) res = res * a % m;
        a = a * a % m;
        b >>= 1;
    }
    return res;
}

class Solution {
public:
    int numSubseq(vector<int>& nums, int target) {
        int n = nums.size(), ans = 0;
        ranges::sort(nums);
        for (int i = 0, j = n - 1; i <= j; ) {
            if (nums[i] + nums[j] > target) j--;
            else {
                ans = (ans + pow(2, j - i, MOD)) % MOD;
                i++;
            }
        } 
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [3,5,6,7]\n9\n
// @lcpr case=end

// @lcpr case=start
// [3,3,6,8]\n10\n
// @lcpr case=end

// @lcpr case=start
// [2,3,3,4,6,7]\n12\n
// @lcpr case=end

 */

