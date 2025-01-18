/*
 * @lc app=leetcode.cn id=5 lang=cpp
 *
 * [5] 最长回文子串
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Manacher {
public:
    string s, t;
    vector<int> halfLen;
    int max_i;
    Manacher(string s) {
        this->s = s;
        t = "^";
        for (char ch : s) {
            t += "#";
            t += ch;
        }
        t += "#$";

        halfLen.resize(t.size() - 2, 0);
        halfLen[1] = 1;
        int boxM = 0, boxR = 0, hl = 1;
        max_i = 0;
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
            if (hl > halfLen[max_i]) {
                max_i = i;
            }
        }
    }

    // 獲取最長回文子字串
    string getMaxPalindrome() {
        int hl = halfLen[max_i];
        return s.substr((max_i - hl) / 2, hl - 1);
    }
};

class Solution {
public:
    string longestPalindrome(string s) {
        Manacher manacher(s);
        return manacher.getMaxPalindrome();
    }
};
// @lc code=end

