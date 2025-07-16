/*
 * @lc app=leetcode.cn id=3201 lang=cpp
 * @lcpr version=30204
 *
 * [3201] 找出有效子序列的最大长度 I
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
    public:
        int maximumLength(vector<int>& nums) {
            vector<int> cnt(2, 0);
            for (int x : nums) cnt[x & 1]++;
            auto f = [&](int b) {
                int res = 0;
                for (int x : nums) {
                    if ((x & 1) == b) {
                        res++;
                        b ^= 1;
                    }
                }
                return res;
            };
            return max({f(0), f(1), cnt[0], cnt[1]});
        }
    };

#include <ranges>
class Solution2 {
public:
    int maximumLength(vector<int>& nums) {
        vector<int> ans(4, 0);
        for (int b : nums | views::transform([](int x) { return x & 1; })) {
            ans[b] += 1;
            ans[2] += (b == (ans[2] & 1));
            ans[3] += (b != (ans[3] & 1));
        }
        return ranges::max(ans);
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end



/*
// @lcpr case=start
// [1,2,3,4]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,1,1,2,1,2]\n
// @lcpr case=end

// @lcpr case=start
// [1,3]\n
// @lcpr case=end

 */

