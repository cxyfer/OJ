/*
 * @lc app=leetcode.cn id=2981 lang=cpp
 *
 * [2981] 找出出现至少三次的最长特殊子字符串 I
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int maximumLength(string s) {
        int n = s.size();
        vector<vector<int>> cnt(26, vector<int>(n+1, 0));
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                bool flag = true;
                for (int k = i+1; k <= j && flag; k++) {
                    if (s[k] != s[i]) {
                        flag = false;
                        break;
                    }
                }
                if (flag) cnt[s[i]-'a'][j-i+1] += 1;
            }
        }
        int ans = -1;
        for (int i = 0; i < 26; i++) {
            for (int j = n; j > 0; j--) {
                if (cnt[i][j] >= 3) {
                    ans = max(ans, j);
                    break;
                }
            }
        }
        return ans;
    }
};
// @lc code=end

