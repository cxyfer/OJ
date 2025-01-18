/*
 * @lc app=leetcode id=1744 lang=cpp
 * @lcpr version=30122
 *
 * [1744] Can You Eat Your Favorite Candy on Your Favorite Day?
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
using LL = long long;
class Solution {
public:
    /*
        Prefix Sum + Reading Test
    */
    vector<bool> canEat(vector<int>& candiesCount, vector<vector<int>>& queries) {
        int n = candiesCount.size(), m = queries.size();
        vector<long long> s(n+1, 0); // prefix sum
        for (int i = 1; i <= n; i++) {
            s[i] = s[i-1] + candiesCount[i-1];
        }
        vector<bool> ans(m, false);
        for (int i = 0; i < m; i++) { // a, b: 1-based; d: 0-based
            int t = queries[i][0], d = queries[i][1], c = queries[i][2];
            LL a = s[t] / c + 1; // 每天都吃 c 顆，最快第 a 天能吃到 Type t 的糖果
            LL b = s[t+1]; // 一天吃一顆，最慢第 b 天能吃到 Type t 的糖果
            ans[i] = a <= d+1 && d+1 <= b;
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [7,4,5,3,8]\n[[0,2,2],[4,2,4],[2,13,1000000000]]\n
// @lcpr case=end

// @lcpr case=start
// [5,2,6,4,1]\n[[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]]\n
// @lcpr case=end

 */

