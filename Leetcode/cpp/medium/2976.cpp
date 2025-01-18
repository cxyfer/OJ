/*
 * @lc app=leetcode.cn id=2976 lang=cpp
 *
 * [2976] 转换字符串的最小成本 I
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    long long minimumCost(string source, string target, vector<char>& original, vector<char>& changed, vector<int>& cost) {
        vector<vector<int>> g(26, vector<int>(26, INT_MAX/2)); // 初始化
        for (int i = 0; i < 26; i++) {
            g[i][i] = 0;
        }
        for (int i = 0; i < original.size(); i++) {
            int u = original[i] - 'a';
            int v = changed[i] - 'a';
            g[u][v] = min(g[u][v], cost[i]); // 這裡要注意，因為可能有重複的邊，所以要取最小值
        }
        // Floyd-Warshall
        for (int k = 0; k < 26; k++) { // 枚舉中間點
            for (int i = 0; i < 26; i++) { // 枚舉起點
                if (g[i][k] == INT_MAX/2) continue; // 不可能由 g[i][k] 轉移到其他點
                for (int j = 0; j < 26; j++) { // 枚舉終點
                    g[i][j] = min(g[i][j], g[i][k] + g[k][j]); // 更新 g[i][j]
                }
            }
        }

        long long ans = 0;
        for (int i = 0; i < source.size(); i++) { // 枚舉每個字元
            int u = source[i] - 'a';
            int v = target[i] - 'a';
            if (g[u][v] == INT_MAX/2) { // 不連通，不可能修改成 target
                return -1;
            }
            ans += g[u][v]; // 將 u 修改成 v 的成本加總
        }
        return ans;
    }
};
// @lc code=end