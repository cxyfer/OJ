    /*
 * @lc app=leetcode.cn id=368 lang=cpp
 * @lcpr version=30204
 *
 * [368] Largest Divisible Subset
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
/*
 * DP: Similar to Longest Increasing Subsequence (LIS)
 * 
 * 重要前提：往一個 Largest Divisible Subset (LDS) 中加入一個數時，**不需檢查所有數**
 * 假設一個 LDS 為 {a, b, c}，其中 a < b < c，則只要滿足以下任一條件，即可將 x 加入 LDS
 * 1. x | a
 * 2. c | x
 * 
 * 至此便可將此問題轉為 Longest Increasing Subsequence (LIS) 問題
*/
// @lc code=start
class Solution1 {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        // f[i] 表示以 nums[i] 結尾的 Largest Divisible Subset
        vector<vector<int>> f(n);
        vector<int> ans;
        for (int i = 0; i < n; i++) {
            f[i].push_back(nums[i]);
            // 枚舉 x = nums[i] 的前一個數 y = nums[j]，若 y | x，則 ∀u, u ∈ f[y] -> u | x
            for (int j = 0; j < i; j++) {
                if (nums[i] % nums[j] == 0) {
                    if (f[i].size() < f[j].size() + 1) {
                        f[i] = f[j];
                        f[i].push_back(nums[i]);
                    }
                }
            }
            // 更新答案
            if (f[i].size() > ans.size()) ans = f[i];
        }
        return ans;
    }
};

class Solution2 {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        // f[i] 表示以 nums[i] 結尾的 Largest Divisible Subset 最大長度
        vector<int> f(n, 1);
        int mx = 0;
        for (int i = 0; i < n; i++) {
            // 枚舉 x = nums[i] 的前一個數 y = nums[j]，若 y | x，則 ∀u, u ∈ f[y] -> u | x
            for (int j = 0; j < i; j++) {
                if (nums[i] % nums[j] == 0) f[i] = max(f[i], f[j] + 1);
            }
            mx = max(mx, f[i]);
        }
        // 從後往前找，找到最大的 LDS
        vector<int> ans;
        for (int i = n - 1; i >= 0 && mx > 0; i--) {
            if (f[i] == mx && (ans.empty() || ans.back() % nums[i] == 0)) {
                ans.push_back(nums[i]);
                mx--;
            }
        }
        return ans;
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end

/*
// @lcpr case=start
// [1,2,3]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,4,8]\n
// @lcpr case=end

 */

