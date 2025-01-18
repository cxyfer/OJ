/*
 * @lc app=leetcode.cn id=647 lang=cpp
 *
 * [647] 回文子串
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int countSubstrings(string s) {
        int n = s.size();
        vector<vector<bool>> dp(n, vector<bool>(n, false));
        int ans = 0;
        for (int i = 0; i < n; ++i) { // 長度為 1 的回文子字串
            dp[i][i] = true;
            ++ans;
        }
        for (int i = 0; i < n - 1; ++i) { // 長度為 2 的回文子字串
            if (s[i] == s[i + 1]) {
                dp[i][i + 1] = true;
                ++ans;
            }
        }
        for (int ln = 3; ln <= n; ++ln) { // 長度 >= 3 的回文子字串
            for (int i = 0; i <= n - ln; ++i) { // 枚舉起始位置
                int j = i + ln - 1; // 終止位置
                if (s[i] == s[j] && dp[i + 1][j - 1]) {
                    dp[i][j] = true;
                    ++ans;
                }
            }
        }
        return ans;
    }
};

class Solution2 {
public:
    int countSubstrings(string s) {
        int n = s.size();
        int ans = 0;
        string t = "^";
        for (char ch : s) {
            t += "#";
            t += ch;
        }
        t += "#$";
        vector<int> halfLen(t.size() - 2, 0);
        halfLen[1] = 1;
        int boxM = 0, boxR = 0, hl = 1;
        for (int i = 2; i < halfLen.size(); i++) {
            hl = 1;
            if (i < boxR) {
                hl = min(halfLen[boxM * 2 - i], boxR - i);
            }
            while (t[i - hl] == t[i + hl]) {
                hl++;
                boxM = i;
                boxR = i + hl;
            }
            halfLen[i] = hl;
            if (i % 2 == 0) { // 偶數位置對應真正的字母，回文子字串長度為奇數
                ans += hl / 2;
            }
            else { // 奇數位置對應 #，回文子字串長度為偶數
                ans += (hl - 1) / 2;
            }
        }
        return ans;
    }
};

// class Solution : public Solution1 {};
class Solution : public Solution2 {};
// @lc code=end
