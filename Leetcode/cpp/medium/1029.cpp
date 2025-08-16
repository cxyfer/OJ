/*
 * @lc app=leetcode.cn id=1029 lang=cpp
 * @lcpr version=30204
 *
 * [1029] 两地调度
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <ranges>

class Solution {
public:
    int twoCitySchedCost(vector<vector<int>>& costs) {
        int n = costs.size() / 2;
        ranges::sort(costs, [](const vector<int>& a, const vector<int>& b) {
            return a[0] - a[1] < b[0] - b[1];
        });
        return ranges::fold_left(views::iota(0, n), 0,
                                 [n, &costs](int s, int i) {
            return s + costs[i][0] + costs[i + n][1];
        });
    }
};
// @lc code=end



/*
// @lcpr case=start
// [[10,20],[30,200],[400,50],[30,20]]\n
// @lcpr case=end

// @lcpr case=start
// [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]\n
// @lcpr case=end

// @lcpr case=start
// [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]\n
// @lcpr case=end

 */

