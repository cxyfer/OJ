/*
 * @lc app=leetcode.cn id=2125 lang=cpp
 * @lcpr version=30204
 *
 * [2125] 银行中的激光束数量
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <ranges>
class Solution {
public:
    int numberOfBeams(vector<string>& bank) {
        vector<int> nums;
        for (auto& row : bank) {
            int cnt = ranges::count(row, '1');
            if (cnt > 0)
                nums.push_back(cnt);
        }
        int ans = 0;
        for (auto [x, y] : views::pairwise(nums))
            ans += x * y;
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// ["011001","000000","010100","001000"]\n
// @lcpr case=end

// @lcpr case=start
// ["000","111","000"]\n
// @lcpr case=end

 */

