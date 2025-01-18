/*
 * @lc app=leetcode.cn id=861 lang=cpp
 *
 * [861] 翻转矩阵后的得分
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    /*
        Greedy
        為使和最大，首先要確保每個row的最高位都是1。
        再來遍歷每一個直行，如果該直行的1的數量小於0的數量，則翻轉該直行，使得該直行的貢獻最大。
    */
    int matrixScore(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        for (int i = 0; i < m; i++) // 確保每個row的最高位都是1
            if (grid[i][0] == 0)
                for (int j = 0; j < n; j++) grid[i][j] ^= 1;

        for (int j = 1; j < n; j++) { // 從第二個col開始，使該col的貢獻最大
            int cnt = 0;
            for (int i = 0; i < m; i++) cnt += grid[i][j];
            if (cnt < m - cnt) // 翻轉的貢獻會比不翻轉大
                for (int i = 0; i < m; i++) grid[i][j] ^= 1;
        }
        int ans = 0; // 計算答案
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                ans += grid[i][j] << (n - 1 - j);
        return ans;
    }
};
// @lc code=end

