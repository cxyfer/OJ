/*
 * @lc app=leetcode.cn id=1717 lang=cpp
 *
 * [1717] 删除子字符串的最大得分
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int maximumGain(string s, int x, int y) {
        int n = s.size();
        if (x < y) {
            for (int i = 0; i < n; i++) {
                if (s[i] == 'a') s[i] = 'b';
                else if (s[i] == 'b') s[i] = 'a';
            }
            swap(x, y);
        }
        int i = 0, ans = 0;
        while (i < n) {
            while (i < n && s[i] != 'a' && s[i] != 'b') i++;
            stack<char> st1;
            while (i < n && (s[i] == 'a' || s[i] == 'b')) {
                if (s[i] == 'a') st1.push('a');
                else {
                    if (!st1.empty() && st1.top() == 'a') {
                        ans += x;
                        st1.pop();
                    } else {
                        st1.push('b');
                    }
                }
                i++;
            }
            stack<char> st2;
            while (!st1.empty()) {
                if (st1.top() == 'a') {
                    st2.push(st1.top());
                    st1.pop();
                } else {
                    if (!st2.empty() && st2.top() == 'a') {
                        ans += y;
                        st1.pop();
                        st2.pop();
                    } else {
                        st2.push(st1.top());
                        st1.pop();
                    }
                }
            }
        }
        return ans;
    }
};

class Solution2 {
public:
    int maximumGain(string s, int x, int y) {
        int n = s.size();
        if (x < y) {
            for (int i = 0; i < n; i++) {
                if (s[i] == 'a') s[i] = 'b';
                else if (s[i] == 'b') s[i] = 'a';
            }
            swap(x, y);
        }
        int i = 0, ans = 0;
        while (i < n) {
            while (i < n && s[i] != 'a' && s[i] != 'b') i++;
            int cnt_a = 0, cnt_b = 0;
            while (i < n && (s[i] == 'a' || s[i] == 'b')) {
                if (s[i] == 'a') cnt_a++;
                else {
                    if (cnt_a > 0) {
                        ans += x;
                        cnt_a--;
                    } else {
                        cnt_b++;
                    }
                }
                i++;
            }
            ans += min(cnt_a, cnt_b) * y;
        }
        return ans;
    }
};

// class Solution : public Solution1 {};
class Solution : public Solution2 {};
// @lc code=end