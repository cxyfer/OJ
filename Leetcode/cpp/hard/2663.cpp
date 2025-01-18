/*
 * @lc app=leetcode.cn id=2663 lang=cpp
 *
 * [2663] 字典序最小的美丽字符串
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    string smallestBeautifulString(string s, int k) {
        int n = s.size();
        k += 'a'; // 用 [a, k + a) 表示 [0, k) 的範圍
        int i = n - 1;
        s[i] += 1;
        while (i < n) {
            if (s[i] == k) { // 需要進位
                if (i == 0) return ""; // 無法進位
                s[i] = 'a';
                s[i - 1] += 1;
                i -= 1;
            } else if (i && s[i] == s[i - 1] || i > 1 && s[i] == s[i - 2]) { // 會形成回文字串
                s[i] += 1;
            } else { // 重新往後檢查是否有回文字串
                i += 1;
            }
        }
        return s;
    }
};
// @lc code=end