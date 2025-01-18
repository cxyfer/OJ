/*
 * @lc app=leetcode.cn id=1626 lang=cpp
 *
 * [1626] 无矛盾的最佳球队
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
/*
    2D Longest Increasing Subsequence (LIS)
    1. Dynamic Programming: O(n^2)
        若 player[j] 可以接在 player[i] 後面，則 player[i] 的 score 和 age 都必須小於等於 player[j] 的 score 和 age
    2. 基於值域計算 : O(nlogn + nU) , U 為 ages 的最大值
        由於 age <= 1e3 ，所以可以基於 age 的值域進行計算。
        首先對 players 依照 score 由小到大排序，若 score 相同則按照 age 由小到大排序。
        令 max_sum[i] 表示 age 最大為 i 的情況下的最大分數和，則 max_sum[age] = max(max_sum[:age+1]) + score
        * 由於排序後確保了 score 是遞增的，所以在已經遍歷過的方案中，並不會出現更大的 score ，也就確保了 max_sum[age] 的正確性。
    3. 基於值域計算 + Binary Indexed Tree (BIT) 優化: O(nlogn + nlogU)
        類似於 2 ，但是使用 BIT 進行優化，可以將 max_sum[age] 的計算從 O(U) 降低到 O(logU)
    Reference:
        - https://leetcode.cn/problems/best-team-with-no-conflicts/solutions/2183029/zui-chang-di-zeng-zi-xu-lie-cong-on2-dao-ojqu/
*/
    int bestTeamScore(vector<int>& scores, vector<int>& ages) {
        // return solve1(scores, ages);
        // return solve2(scores, ages);
        return solve3(scores, ages);
    }
    int solve1(vector<int>& scores, vector<int>& ages) {
        int n = scores.size();
        vector<pair<int, int>> players;
        for (int i = 0; i < n; i++) players.push_back({ages[i], scores[i]});
        sort(players.begin(), players.end());
        vector<int> dp(n);
        int ans = 0;
        for (int j = 0; j < n; j++) {
            dp[j] = players[j].second;
            for (int i = 0; i < j; i++) {
                if (players[i].second <= players[j].second) { // j 可以接在 i 後面
                    dp[j] = max(dp[j], dp[i] + players[j].second);
                }
            }
            ans = max(ans, dp[j]);
        }
        return ans;
    }
    int solve2(vector<int>& scores, vector<int>& ages) {
        int n = scores.size(), mx = 0, ans = 0;
        vector<pair<int, int>> players;
        for (int i = 0; i < n; i++){
            players.push_back({scores[i], ages[i]});
            mx = max(mx, ages[i]);
        }
        sort(players.begin(), players.end()); // sort by score
        vector<int> max_sum(mx+1, 0);
        for (auto p : players) {
            int score = p.first, age = p.second;
            for (int i = age-1; i >= 0; i--) {
                max_sum[age] = max(max_sum[age], max_sum[i]);
            }
            max_sum[age] += score;
            ans = max(ans, max_sum[age]);
        }
        return ans;
    }
    int solve3(vector<int>& scores, vector<int>& ages) {
        int n = scores.size(), mx = 0;
        vector<pair<int, int>> players;
        for (int i = 0; i < n; i++){
            players.push_back({scores[i], ages[i]});
            mx = max(mx, ages[i]);
        }
        sort(players.begin(), players.end()); // sort by score
        vector<int> tree(mx+1, 0);

        auto update = [&](int k, int x) {
            for  (int i = k; i <= mx; i += i & -i) {
                tree[i] = max(tree[i], x);
            }
        };
        auto query = [&](int k) {
            int res = 0;
            for (int i = k; i > 0; i -= i & -i) {
                res = max(res, tree[i]);
            }
            return res;
        };
        for (auto p : players) {
            int score = p.first, age = p.second;
            update(age, query(age) + score);
        }
        return query(mx);
    }
};
// @lc code=end

