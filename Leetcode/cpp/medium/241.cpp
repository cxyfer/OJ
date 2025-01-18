/*
 * @lc app=leetcode.cn id=241 lang=cpp
 *
 * [241] 为运算表达式设计优先级
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    const int ADD = -1;
    const int SUB = -2;
    const int MUL = -3;
    vector<int> diffWaysToCompute(string expression) {
        int n = expression.size();
        vector<int> tokens;
        int i = 0, num = 0;
        while (i < n) {
            if (isdigit(expression[i])) {
                num = 0;
                while (i < n && isdigit(expression[i])) {
                    num = num * 10 + (expression[i++] - '0');
                }
                tokens.push_back(num);
            } else {
                if (expression[i] == '+') {
                    tokens.push_back(ADD);
                } else if (expression[i] == '-') {
                    tokens.push_back(SUB);
                } else {
                    tokens.push_back(MUL);
                }
                i++;
            }
        }

        int m = tokens.size();
        unordered_map<int, vector<int>> memo;
        function<vector<int>(int, int)> dfs = [&](int l, int r) -> vector<int> {
            if (memo.find(l * m + r) != memo.end()) {
                return memo[l * m + r];
            }
            vector<int> &res = memo[l * m + r];
            if (l == r) {
                res.push_back(tokens[l]);
                return res;
            }
            for (int i = l; i < r; i += 2) {
                int op = tokens[i + 1];
                auto left = dfs(l, i);
                auto right = dfs(i + 2, r);
                for (auto & x : left) {
                    for (auto & y : right) {
                        if (op == ADD) {
                            res.push_back(x + y);
                        } else if (op == SUB) {
                            res.push_back(x - y);
                        } else {
                            res.push_back(x * y);
                        }
                    }
                }
            }
            return res;
        };
        return dfs(0, m - 1);
    }
};
// @lc code=end

