/*
 * @lc app=leetcode.cn id=131 lang=cpp
 *
 * [131] 分割回文串
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<vector<string>> partition(string s) {
        int n = s.size();
        vector<vector<bool>> is_palindrome(n, vector<bool>(n, false));
        for (int i = 0; i < n; i++) is_palindrome[i][i] = true; // 長度 1
        for (int k = 2; k <= n; k++) { // 枚舉長度 k
            for (int i = 0; i < n - k + 1; i++) { // 枚舉起點 i
                int j = i + k - 1; // 對應的終點 j
                if (s[i] == s[j] && (k == 2 || is_palindrome[i + 1][j - 1])) { // 頭尾相同，若 長度為2 或 內部也是回文(從 is_palindrome[i+1][j-1] 轉移) ，則是回文
                    is_palindrome[i][j] = true;
                }
            }
        }
        vector<vector<string>> ans;
        vector<string> path;
        function<void(int)> dfs = [&](int i) {
            if (i == n) {
                ans.push_back(path);
                return;
            }
            for (int j = i; j < n; j++) { // 枚舉終點 j
                if (is_palindrome[i][j]) {
                    path.push_back(s.substr(i, j - i + 1));
                    dfs(j + 1);
                    path.pop_back();
                }
            }
        };
        dfs(0);
        return ans;
    }
};
// @lc code=end

