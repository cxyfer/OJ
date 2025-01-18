/*
 * @lc app=leetcode.cn id=2597 lang=cpp
 *
 * [2597] 美丽子集的数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int beautifulSubsets(vector<int>& nums, int k) {
        // return solve1a(nums, k);
        // return solve1b(nums, k);
        return solve2(nums, k);
    }
    int solve1a(vector<int>& nums, int k) {
        int n = nums.size();
        int ans = 0, mx = *max_element(nums.begin(), nums.end());
        vector<int> cnt(mx + 2 * k + 1, 0);
        function<void(int)> dfs = [&](int i) { // 第一種：選或不選
            if (i == n) {
                ans += 1;
                return;
            }
            dfs(i + 1); // 不選
            int x = nums[i] + k; // 避免索引為負數
            if (cnt[x - k] == 0 && cnt[x + k] == 0) { // 滿足條件
                cnt[x] += 1;
                dfs(i + 1); // 選
                cnt[x] -= 1;
            }
        };
        dfs(0);
        return ans - 1; // 減去空集合
    }
    int solve1b(vector<int>& nums, int k) {
        int n = nums.size();
        int ans = 0, mx = *max_element(nums.begin(), nums.end());
        vector<int> cnt(mx + 2 * k + 1, 0);
        function<void(int)> dfs = [&](int i) { // 第二種：枚舉下一個選哪個
            ans += 1;
            for (int j = i; j < n; j++) { // 枚舉下一個選的是哪個
                int x = nums[j] + k; // 避免索引為負數
                if (cnt[x - k] == 0 && cnt[x + k] == 0) { // 滿足條件
                    cnt[x] += 1;
                    dfs(j + 1);
                    cnt[x] -= 1;
                }
            }
        };
        dfs(0);
        return ans - 1; // 減去空集合
    }
    int solve2(vector<int>& nums, int k) {
        unordered_map<int, map<int, int>> groups;
        for (int x : nums) {
            groups[x % k][x]++;
        }
        int ans = 1;
        for (auto group : groups) { // (key, cnt)
            auto& cnt = group.second;
            int m = cnt.size();
            vector<int> dp(m + 1, 0); // dp[i] 表示前 i 個數字的方案數，1-indexed
            auto it = cnt.begin();
            dp[0] = 1;
            dp[1] = 1 << it++->second; // 初始化 dp[1] 為 不選和選第一個
            for (int i = 1; i < m; i++, it++) {
                int x = it->first;
                if (x - prev(it)->first == k) { // 和前一個相差為 k ，則不能同時選 keys[i] 和 keys[i-1]
                    dp[i + 1] = dp[i] + dp[i - 1] * ((1 << it->second) - 1);
                } else { // 和前一個相差不為 k ，則可以同時選 keys[i] 和 keys[i-1]
                    dp[i + 1] = dp[i] << it->second;
                }
            }
            ans *= dp[m]; // 乘法原理
        }
        return ans - 1; // 去除空集合
    }
};
// @lc code=end

