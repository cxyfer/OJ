/*
 * @lc app=leetcode.cn id=3522 lang=cpp
 * @lcpr version=30204
 *
 * [3522] 执行指令后的得分
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    long long calculateScore(vector<string>& instructions, vector<int>& values) {
        int n = instructions.size();
        long long ans = 0;
        vector<bool> vis(n);
        for (int i = 0; 0 <= i && i < n && !vis[i]; ) {
            vis[i] = true;
            if (instructions[i][0] == 'j') i += values[i];
            else ans += values[i++];
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// ["jump","add","add","jump","add","jump"]\n[2,1,3,1,-2,-3]\n
// @lcpr case=end

// @lcpr case=start
// ["jump","add","add"]\n[3,1,1]\n
// @lcpr case=end

// @lcpr case=start
// ["jump"]\n[0]\n
// @lcpr case=end

 */

