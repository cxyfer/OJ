/*
 * @lc app=leetcode.cn id=1910 lang=cpp
 *
 * [1910] 删除一个字符串中所有出现的给定子字符串
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    string removeOccurrences(string s, string part) {
        for (auto it = s.find(part); it != string::npos; it = s.find(part))
            s.erase(it, part.length());
        return s;
    }
};

class Solution2 {
public:
    string removeOccurrences(string s, string part) {
        string st;
        for (auto ch : s) {
            st.push_back(ch);
            if (st.size() >= part.size() && st.substr(st.size() - part.size()) == part)
                st.resize(st.size() - part.size());
        }
        return st;
    }
};

class Solution3 {
public:
    string removeOccurrences(string s, string part) {
        int n = s.size(), m = part.size();
        vector<int> pi(m);
        int ln = 0;
        for (int i = 1; i < m; i++) {
            while (ln && part[i] != part[ln])
                ln = pi[ln - 1];
            if (part[i] == part[ln])
                ln++;
            pi[i] = ln;
        }
        vector<char> ans(n);
        vector<int> pi2(n + 1);
        int sz = 0;
        for (auto ch : s) {
            ans[sz] = ch;
            ln = pi2[sz];
            sz++;
            while (ln && ch != part[ln])
                ln = pi[ln - 1];
            if (ch == part[ln])
                ln++;
            pi2[sz] = ln;
            if (ln == m)
                sz -= m;
        }
        return string(ans.begin(), ans.begin() + sz);
    }
};

// class Solution : public Solution1 {};
// class Solution : public Solution2 {};
class Solution : public Solution3 {};
// @lc code=end
