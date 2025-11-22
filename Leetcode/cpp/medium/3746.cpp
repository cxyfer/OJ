/*
 * @lc app=leetcode.cn id=3746 lang=cpp
 * @lcpr version=30204
 *
 * [3746] 等量移除后的字符串最小长度
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int minLengthAfterRemovals(string s) {
        return abs(2 * count(s.cbegin(), s.cend(), 'a') - static_cast<int>(s.size()));
    }
};
// @lc code=end



/*
// @lcpr case=start
// "aabbab"\n
// @lcpr case=end

// @lcpr case=start
// "aaaa"\n
// @lcpr case=end

// @lcpr case=start
// "aaabb"\n
// @lcpr case=end

 */

