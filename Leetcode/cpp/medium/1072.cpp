/*
 * @lc app=leetcode.cn id=1072 lang=cpp
 *
 * [1072] 按列翻转得到最大值等行数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
const int N = 300;
class Solution {
public:
    int maxEqualRowsAfterFlips(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        bitset<N> mask;
        for (int i = 0; i < n; ++i) mask[i] = 1;
        unordered_map<bitset<N>, int> cnt;
        for (auto& row : matrix) {
            bitset<N> x;
            for (int i = 0; i < n; ++i) if (row[i]) x[i] = 1;
            cnt[row[0] ? x ^ mask : x]++;
        }
        int ans = 0;
        for (auto& [_, v] : cnt) ans = max(ans, v);
        return ans;
    }
};
// @lc code=end

