/*
 * @lc app=leetcode.cn id=38 lang=cpp
 * @lcpr version=30204
 *
 * [38] 外观数列
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
const int MX_N = 30;
vector<string> ans(MX_N + 1);
auto init = []() {
    auto say = [](string s) {
        int n = s.size();
        string res;
        for (int i = 0, j = 0; i < n; j = i) {
            while (i < n && s[i] == s[j]) i++;
            res += to_string(i - j) + s[j];
        }
        return res;
    };
    ans[1] = "1";
    for (int i = 2; i <= MX_N; i++)
        ans[i] = say(ans[i-1]);
    return 0;
}();

class Solution {
public:
    string countAndSay(int n) {
        return ans[n];
    }
};
// @lc code=end



/*
// @lcpr case=start
// 4\n
// @lcpr case=end

// @lcpr case=start
// 1\n
// @lcpr case=end

 */

