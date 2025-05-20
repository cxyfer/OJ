/*
 * @lc app=leetcode.cn id=3489 lang=cpp
 * @lcpr version=30204
 *
 * [3489] 零数组变换 IV
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int minZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size(), m = queries.size();
        vector<int> ids(n);
        iota(ids.begin(), ids.end(), 0);

        // 如果所有 nums[i] 都是 0，則直接返回 0
        if (all_of(ids.begin(), ids.end(), [&](int i) { return nums[i] == 0; }))
            return 0;

        // 初始化 f[i][j] 表示第 i 個位置是否能夠湊出 j
        vector<vector<bool>> f(n);
        for (int i = 0; i < n; i++) {
            f[i] = vector<bool>(nums[i] + 1, false);
            f[i][0] = true;
        }

        // 遍歷所有查詢
        for (int k = 0; k < m; k++) {
            int l = queries[k][0], r = queries[k][1], v = queries[k][2];
            // 更新 [l, r] 區間
            for (int i = l; i <= r; i++) {
                int x = nums[i];
                if (f[i][x]) continue;  // 如果已經湊出 nums[i]，則跳過
                // 從大到小更新 f[i][j]
                for (int j = x; j >= v; j--)
                    f[i][j] = f[i][j] || f[i][j - v];
            }
            // 檢查是否能夠湊出所有的 nums[i]
            if (all_of(ids.begin(), ids.end(), [&](int i) { return f[i][nums[i]]; }))
                return k + 1;
        }
        return -1;
    }
};

class Solution2 {
public:
    int minZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size(), m = queries.size();
        vector<int> ids(n);
        iota(ids.begin(), ids.end(), 0);

        // 如果所有 nums[i] 都是 0，則直接返回 0
        if (all_of(ids.begin(), ids.end(), [&](int i) { return nums[i] == 0; }))
            return 0;

        // 初始化 f[i] 表示第 i 個位置能夠湊出的所有可能值，用位運算表示
        vector<bitset<1001>> f(n);
        for (int i = 0; i < n; i++)
            f[i] = 1;

        // 遍歷所有查詢
        for (int k = 0; k < m; k++) {
            int l = queries[k][0], r = queries[k][1], v = queries[k][2];
            // 更新 [l, r] 區間
            for (int i = l; i <= r; i++) {
                int x = nums[i];
                if (f[i][x]) continue;  // 如果已經湊出 nums[i]，則跳過
                f[i] |= f[i] << v;
            }
            // 檢查是否能夠湊出所有的 nums[i]
            if (all_of(ids.begin(), ids.end(), [&](int i) { return f[i][nums[i]]; }))
                return k + 1;
        }
        return -1;
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end


/*
// @lcpr case=start
// [2,0,2]\n[[0,2,1],[0,2,1],[1,1,3]]\n
// @lcpr case=end

// @lcpr case=start
// [4,3,2,1]\n[[1,3,2],[0,2,1]]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,2,1]\n[[0,1,1],[1,2,1],[2,3,2],[3,4,1],[4,4,1]]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,2,6]\n[[0,1,1],[0,2,1],[1,4,2],[4,4,4],[3,4,1],[4,4,5]]\n
// @lcpr case=end

 */

