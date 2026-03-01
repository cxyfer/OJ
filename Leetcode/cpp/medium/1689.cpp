/*
 * @lc app=leetcode.cn id=1689 lang=cpp
 * @lcpr version=30204
 *
 * [1689] 十-二进制数的最少数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <ranges>

class Solution {
public:
    int minPartitions(string n) {
        return ranges::max(n) - '0';
    }
};
// @lc code=end



/*
// @lcpr case=start
// "32"\n
// @lcpr case=end

// @lcpr case=start
// "82734"\n
// @lcpr case=end

// @lcpr case=start
// "27346209830709182346"\n
// @lcpr case=end

 */

