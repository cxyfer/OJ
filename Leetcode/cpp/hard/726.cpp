/*
 * @lc app=leetcode.cn id=726 lang=cpp
 *
 * [726] 原子的数量
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    string countOfAtoms(string formula) {
        int n = formula.size(), i = 0;
        stack<map<string, int>> st;
        st.push({});
        while (i < n) {
            if (formula[i] == '(') {
                st.push({});
                i++;
            } else if (formula[i] == ')') {
                i++;
                int mul = 0;
                while (i < n && isdigit(formula[i])) mul = mul * 10 + formula[i++] - '0';
                mul = mul == 0 ? 1 : mul;
                auto cnt = st.top();
                st.pop();
                for (auto [k, v] : cnt) st.top()[k] += v * mul;
            } else {
                string elem = formula.substr(i++, 1);
                while (i < n && islower(formula[i])) elem += formula[i++];
                int mul = 0;
                while (i < n && isdigit(formula[i])) mul = mul * 10 + formula[i++] - '0';
                mul = mul == 0 ? 1 : mul;
                st.top()[elem] += mul;
            }
        }
        auto cnt = st.top();
        string ans;
        for (auto [k, v] : cnt) ans += k + (v > 1 ? to_string(v) : "");
        return ans;
    }
};
// @lc code=end