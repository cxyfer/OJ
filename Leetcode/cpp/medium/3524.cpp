/*
 * @lc app=leetcode.cn id=3524 lang=cpp
 * @lcpr version=30204
 *
 * [3524] 求出数组的 X 值 I
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
using LL = long long;
class Solution1 {
public:
    vector<LL> resultArray(vector<int>& nums, int k) {
        int n = nums.size();
        vector<LL> ans(k);
        vector<vector<LL>> f(n + 1, vector<LL>(k));
        for (int i = 1; i <= n; i++) {
            int v = nums[i - 1] % k;
            f[i][v]++;
            for (int j = 0; j < k; j++)
                f[i][(j * v) % k] += f[i - 1][j];
            for (int j = 0; j < k; j++)
                ans[j] += f[i][j];
        }
        return ans;
    }
};

class Solution2 {
public:
    vector<LL> resultArray(vector<int>& nums, int k) {
        int n = nums.size();
        vector<LL> ans(k), f(k), nf(k);
        for (int i = 0; i < n; i++) {
            fill(nf.begin(), nf.end(), 0);
            int v = nums[i] % k;
            nf[v]++;
            for (int j = 0; j < k; j++)
                nf[(j * v) % k] += f[j];
            for (int j = 0; j < k; j++)
                ans[j] += nf[j];
            f.swap(nf);
        }
        return ans;
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end



/*
// @lcpr case=start
// [1,2,3,4,5]\n3\n
// @lcpr case=end

// @lcpr case=start
// [1,2,4,8,16,32]\n4\n
// @lcpr case=end

// @lcpr case=start
// [1,1,2,1,1]\n2\n
// @lcpr case=end

 */

