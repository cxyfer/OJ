/*
 * @lc app=leetcode.cn id=2011 lang=cpp
 * @lcpr version=30204
 *
 * [2011] 执行操作后的变量值
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int ans = 0;
        for (auto& op : operations)
            if (op[1] == '+') ans++;
            else ans--;
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// ["--X","X++","X++"]\n
// @lcpr case=end

// @lcpr case=start
// ["++X","++X","X++"]\n
// @lcpr case=end

// @lcpr case=start
// ["X++","++X","--X","X--"]\n
// @lcpr case=end

 */

