/*
 * @lc app=leetcode.cn id=1598 lang=cpp
 *
 * [1598] 文件夹操作日志搜集器
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int minOperations(vector<string>& logs) {
        int ans = 0;
        for (auto& log : logs) {
            if (log == "./") continue;
            if (log == "../") ans = max(ans - 1, 0);
            else ans++;
        }
        return ans;
    }
};
// @lc code=end

