/*
 * @lc app=leetcode.cn id=73 lang=cpp
 *
 * [73] 矩阵置零
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    /*
        1. 使用額外 O(n) 空間標記。
            使用兩個陣列 row 和 col 來標記原陣列的行和列是否包含 0
        2. 使用原陣列的第一直行和第一橫列作為標記。
            但由於標記會破壞原本的數據，所以需要另外使用兩個變量來標記原本的第一直行和第一橫列是否包含 0
            置 0 時先忽略第一直行和第一橫列，從第二直行和第二橫列開始，最後再根據兩個變量來處理第一直行和第一橫列
        3. 從 2. 進一步優化，同樣使用原陣列的第一直行和第一橫列作為標記，但可以只使用一個額外變數來標記原本的第一直行是否包含 0
            將原陣列的第一橫列是否包含 0 的標記放在 matrix[0][0] 中，如此就只需要標記原本的第一直行是否包含 0
            標記時從 每一橫列 的 第二直行 開始，
            由於會用到第一橫列的資訊，置零時先忽略第一橫列，從第二橫列開始
            同樣地，由於會用到第一直行的資訊，在置零每一橫列時，將第一直行留在該橫列的最後處理。
    */
    void setZeroes(vector<vector<int>>& matrix) {
        // solve1(matrix);
        // solve2(matrix);
        solve3(matrix);
    }
    void solve1(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        vector<bool> row(m, false), col(n, false);
        for (int i = 0; i < m; i++) { // 標記
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 0) row[i] = col[j] = true;
            }
        }
        for (int i = 0; i < m; i++) { // 置零
            for (int j = 0; j < n; j++) {
                if (row[i] || col[j])  matrix[i][j] = 0;
            }
        }
    }
    void solve2(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        bool col0 = false, row0 = false;
        for (int i = 0; i < m; i++) if (matrix[i][0] == 0) col0 = true; // 原陣列的第一直行是否有 0
        for (int j = 0; j < n; j++) if (matrix[0][j] == 0) row0 = true; // 原陣列的第一橫列是否有 0
        for (int i = 1; i < m; i++) { // 用原陣列的第一直行和第一橫列作為標記
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == 0) matrix[i][0] = matrix[0][j] = 0;
            }
        }
        for (int i = 1; i < m; i++) { // 對除了第一直行和第一橫列以外的部分進行置零
            for (int j = 1; j < n; j++) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0)  matrix[i][j] = 0;
            }
        }
        if (col0) for (int i = 0; i < m; i++) matrix[i][0] = 0; // 置零第一直行
        if (row0) for (int j = 0; j < n; j++) matrix[0][j] = 0; // 置零第一橫列
    }
    void solve3(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        bool col0 = false;
        for (int i = 0; i < m; i++) {  // 標記
            if (matrix[i][0] == 0) col0 = true; // 原陣列的第一直行是否有 0
            for (int j = 1; j < n; j++) { // 用原陣列的第一直行和第一橫列作為標記
                if (matrix[i][j] == 0) matrix[i][0] = matrix[0][j] = 0;
            }
        }
        for (int i = 1; i < m; i++) { // 從第二橫列開始置零
            for (int j = 1; j < n; j++) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0)  matrix[i][j] = 0;
            }
            if (col0) matrix[i][0] = 0; // 置零該行列的第一直行
        }
        if (matrix[0][0] == 0) for (int j = 1; j < n; j++) matrix[0][j] = 0; // 置零第一橫列
        if (col0) matrix[0][0] = 0;
    }
};
// @lc code=end

