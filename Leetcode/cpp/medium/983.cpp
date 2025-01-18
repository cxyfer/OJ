/*
 * @lc app=leetcode.cn id=983 lang=cpp
 *
 * [983] 最低票价
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
/*
1. 記憶化搜索 O(D)
2. 基於值域的迭代 O(D)
3. 基於日期，三指標 O(n)
*/
// @lc code=start
class Solution1 {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        unordered_set<int> days_set(days.begin(), days.end());
        int first_day = days[0], last_day = days.back();

        // memo[i] 表示從第 i 天開始旅行的最小花費
        vector<int> memo(last_day + 1, -1);
        function<int(int)> dfs = [&](int i) -> int {
            if (i > last_day) return 0;
            int &res = memo[i];
            if (res != -1) return res;
            if (days_set.count(i)) { // 第 i 天需要買票，則比較三種買票方案的花費，取最小值
                res = min({costs[0] + dfs(i + 1), costs[1] + dfs(i + 7), costs[2] + dfs(i + 30)});
            } else { // 第 i 天不需要買票，可以跳過
                res = dfs(i + 1);
            }
            return res;
        };
        return dfs(first_day);
    }
};

class Solution2 {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        unordered_set<int> days_set(days.begin(), days.end());
        int first_day = days[0], last_day = days.back();
        // dp[i] 表示從第 i 天開始旅行的最小花費
        vector<int> dp(last_day + 31, 0); // 多開 30 天，避免索引越界
        for (int i = last_day; i >= first_day; --i) {
            if (days_set.count(i)) {
                dp[i] = min({costs[0] + dp[i + 1], costs[1] + dp[i + 7], costs[2] + dp[i + 30]});
            } else {
                dp[i] = dp[i + 1];
            }
        }
        return dp[first_day];
    }
};

class Solution3 {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        int n = days.size();
        // dp[i] 表示從 days[i] 開始旅行的最小花費
        vector<int> dp(n + 1, 0);
        // j 和 k 分別表示若當前購買 7 天票和 30 天票，則可以不用買票的「最大」日期下標
        int j = n - 1, k = n - 1; 
        for (int i = n - 1; i >= 0; --i) {
            while (days[j] >= days[i] + 7) --j;
            while (days[k] >= days[i] + 30) --k;
            // 轉移方程，j + 1 和 k + 1 是下次需要買票的日期
            dp[i] = min({costs[0] + dp[i + 1], costs[1] + dp[j + 1], costs[2] + dp[k + 1]});
        }
        return dp[0];
    }
};

class Solution : public Solution1 {};
// class Solution : public Solution2 {};
// class Solution : public Solution3 {};
// @lc code=end