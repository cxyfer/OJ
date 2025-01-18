/*
 * @lc app=leetcode.cn id=1738 lang=cpp
 *
 * [1738] 找出第 K 大的异或坐标值
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int kthLargestValue(vector<vector<int>>& matrix, int k) {
        // return solve1(matrix, k);
        return solve2(matrix, k);
    }
    int solve1(vector<vector<int>>& matrix, int k) {
        int m =  matrix.size(), n = matrix[0].size();
        vector<vector<int>> pre(m+1, vector<int>(n+1, 0));
        vector<int> res;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                pre[i+1][j+1] = pre[i+1][j] ^ pre[i][j+1] ^ pre[i][j] ^ matrix[i][j];
                res.push_back(pre[i+1][j+1]);
            }
        }
        sort(res.begin(), res.end(), greater<int>());
        return res[k-1];
    }
    int solve2(vector<vector<int>>& matrix, int k) {
        int m =  matrix.size(), n = matrix[0].size();
        vector<vector<int>> pre(m+1, vector<int>(n+1, 0));
        priority_queue<int, vector<int>, greater<int>> hp; // Min Heap of size k
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                pre[i+1][j+1] = pre[i+1][j] ^ pre[i][j+1] ^ pre[i][j] ^ matrix[i][j];
                hp.push(pre[i+1][j+1]);
                if (hp.size() > k) hp.pop();
            }
        }
        return hp.top();
    }
};
// @lc code=end

