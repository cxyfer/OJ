/*
 * @lc app=leetcode.cn id=378 lang=cpp
 * @lcpr version=30204
 *
 * [378] 有序矩阵中第 K 小的元素
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int n = matrix.size(), m = matrix[0].size();
        auto check = [&](int mx) -> bool {
            int cnt = 0;
            for (int i = 0, j = m - 1; i < n && j >= 0 && cnt < k; i++) {
                while (j >= 0 && matrix[i][j] > mx) j--;
                cnt += j + 1;
            }
            return cnt >= k;
        };
        int left = matrix[0][0], right = matrix[n - 1][m - 1];
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (check(mid)) right = mid - 1;
            else left = mid + 1;
        }
        return left;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [[1,5,9],[10,11,13],[12,13,15]]\n8\n
// @lcpr case=end

// @lcpr case=start
// [[-5]]\n1\n
// @lcpr case=end

 */

