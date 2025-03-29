/*
 * @lc app=leetcode.cn id=3233 lang=cpp
 * @lcpr version=30204
 *
 * [3233] 统计不是特殊数字的数字数量
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
const int MAXN = 1e9 + 5;
const int MAXN_SQRT = sqrt(MAXN);

vector<bool> is_prime(MAXN_SQRT + 1, true);
vector<int> nums;
auto init = []() {
    is_prime[0] = is_prime[1] = false;
    for (int i = 2; i <= MAXN_SQRT; i++) {
        if (is_prime[i]) {
            for (int j = i * i; j <= MAXN_SQRT; j += i)
                is_prime[j] = false;
            nums.push_back(i * i);
        }
    }
    return 0;
}();

class Solution {
public:
    int nonSpecialCount(int l, int r) {
        return r - l + 1 - (upper_bound(nums.begin(), nums.end(), r) - lower_bound(nums.begin(), nums.end(), l));
    }
};
// @lc code=end



/*
// @lcpr case=start
// 5\n7\n
// @lcpr case=end

// @lcpr case=start
// 4\n16\n
// @lcpr case=end

 */

