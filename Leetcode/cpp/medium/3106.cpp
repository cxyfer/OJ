/*
 * @lc app=leetcode.cn id=3106 lang=cpp
 *
 * [3106] 满足距离约束且字典序最小的字符串
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    string getSmallestString(string s, int k) {
        for (int i = 0; i < s.size(); i++) {
            int dis = min(s[i] - 'a', 'z' - s[i] + 1);
            if (dis > k) {
                s[i] = s[i] - k;
                break;
            }
            s[i] = 'a';
            k -= dis;
        }
        return s;
    }
};
// @lc code=end

