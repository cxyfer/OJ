/*
 * @lc app=leetcode.cn id=344 lang=cpp
 *
 * [344] 反转字符串
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    void reverseString(vector<char>& s) {
        // solve1(s);
        solve2(s);
    }
    void solve1(vector<char>& s) {
        int n = s.size();
        for (int i = 0; i < n / 2; i++) swap(s[i], s[n - i - 1]);
    }
    void solve2(vector<char>& s) {
        int i = 0, j = s.size() - 1;
        while (i < j) swap(s[i++], s[j--]);
    }
};
// @lc code=end

