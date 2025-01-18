/*
 * @lc app=leetcode.cn id=1105 lang=cpp
 *
 * [1105] 填充书架
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int minHeightShelves(vector<vector<int>>& books, int shelfWidth) {
        int n = books.size();
        vector<unordered_map<int, unordered_map<int, int>>> memo(n);
        function<int(int, int, int)> dfs = [&](int i, int cur_w, int cur_h) {
            if (i == n) return cur_h;
            if (memo[i].count(cur_w) && memo[i][cur_w].count(cur_h)) return memo[i][cur_w][cur_h];
            int res = cur_h + dfs(i + 1, books[i][0], books[i][1]); // 放到下一層
            if (cur_w + books[i][0] <= shelfWidth) { // 可以放到同一層
                res = min(res, dfs(i + 1, cur_w + books[i][0], max(cur_h, books[i][1])));
            }
            return memo[i][cur_w][cur_h] = res;
        };
        return dfs(0, 0, 0);
    }
};

class Solution2 {
public:
    int minHeightShelves(vector<vector<int>>& books, int shelfWidth) {
        int n = books.size();
        vector<int> memo(n, -1);
        function<int(int)> dfs = [&](int i) {
            if (i == n) return 0;
            if (memo[i] != -1) return memo[i];
            int res = float('inf');
            int max_h = 0, left_w = shelfWidth;
            for (int j = i; j < n; ++j) {
                left_w -= books[j][0];
                if (left_w < 0) break; // 無法將 books[i], ... , books[j] 放到同一層
                max_h = max(max_h, books[j][1]); // 更新最大高度
                res = min(res, max_h + dfs(j + 1)); // 遞迴到子問題
            }
            return memo[i] = res;
        };
        return dfs(0);
    }
};

// class Solution: public Solution1 {};
class Solution: public Solution2 {};
// @lc code=end