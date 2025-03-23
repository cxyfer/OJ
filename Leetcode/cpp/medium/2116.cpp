/*
 * @lc app=leetcode.cn id=2116 lang=cpp
 * @lcpr version=30204
 *
 * [2116] 判断一个括号字符串是否有效
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
/*
 * 1. Greedy (Two-pass)
 *   - 確保從左到右的能變成 '(' 的數量大於 ')' 的數量，反之同理
 * 2. Greedy (One-pass)
 *   - Similar to 678. Valid Parenthesis String
 *   - 維護可能的 cnt 取值範圍
*/
// @lc code=start
class Solution1 {
public:
    bool canBeValid(string s, string locked) {
        int n = s.size();
        if (n & 1) return false;
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (s[i] == '(' || locked[i] == '0') cnt++;
            else {
                cnt--;
                if (cnt < 0) return false;
            }
        }
        cnt = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (s[i] == ')' || locked[i] == '0') cnt++;
            else {
                cnt--;
                if (cnt < 0) return false;
            }
        }
        return true;
    }
};

class Solution2 {
public:
    bool canBeValid(string s, string locked) {
        int n = s.size();
        if (n & 1) return false;
        int mn = 0, mx = 0;
        for (int i = 0; i < n; i++) {
            if (locked[i] == '1') {
                if (s[i] == '(') {
                    mn++;
                    mx++;
                }
                else {
                    mn = max(0, mn - 1);
                    mx--;
                    if (mx < 0) return false;
                }
            }
            else {
                mn = max(0, mn - 1);
                mx++;
            }
        }
        return mn == 0;
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end



/*
// @lcpr case=start
// "))()))"\n"010100"\n
// @lcpr case=end

// @lcpr case=start
// "()()"\n"0000"\n
// @lcpr case=end

// @lcpr case=start
// ")"\n"0"\n
// @lcpr case=end

// @lcpr case=start
// "(((())(((())"\n"111111010111"\n
// @lcpr case=end

 */

