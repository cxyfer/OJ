/*
 * @lc app=leetcode.cn id=1526 lang=cpp
 * @lcpr version=30204
 *
 * [1526] 形成目标数组的子数组最少增加次数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <ranges>

class Solution {
public:
    int minNumberOperations(vector<int>& target) {
        int ans = target[0];
        for (auto [x, y] : views::pairwise(target))
            ans += max(0, y - x);
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,2,3,2,1]\n
// @lcpr case=end

// @lcpr case=start
// [3,1,1,2]\n
// @lcpr case=end

// @lcpr case=start
// [3,1,5,4,2]\n
// @lcpr case=end

// @lcpr case=start
// [1,1,1,1]\n
// @lcpr case=end

 */

