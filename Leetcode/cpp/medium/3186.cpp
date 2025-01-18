/*
 * @lc app=leetcode id=3186 lang=cpp
 *
 * [3186] Maximum Total Damage With Spell Casting
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
using LL = long long;

class Solution1 {
public:
    long long maximumTotalDamage(vector<int>& power) {
        unordered_map<int, int> cnt;
        for (int x : power) cnt[x]++;
        vector<pair<int, int>> kv(cnt.begin(), cnt.end());
        sort(kv.begin(), kv.end());
        int m = kv.size();

        vector<LL> dp(m, 0), mx(m, 0);
        dp[0] = (LL)kv[0].first * kv[0].second;
        mx[0] = dp[0];
        for (int i = 1; i < m; i++) {
            for (int j = i - 1; j >= 0; j--) {
                int d = kv[i].first - kv[j].first;
                if (d == 1 || d == 2) continue;
                dp[i] = max(dp[i], mx[j]);
                break;
            }
            dp[i] += (LL)kv[i].first * kv[i].second;
            mx[i] = max(mx[i - 1], dp[i]);
        }
        return *max_element(dp.begin(), dp.end());
    }
};

class Solution2 {
public:
    long long dfs(int i, vector<pair<int, int>>& kv, vector<LL>& memo) {
        if (i < 0) return 0;
        LL &res = memo[i];
        if (res != -1) return res;
        int j = i - 1;
        while (j >= 0 && kv[i].first - kv[j].first <= 2) j--;
        return res = max(dfs(i - 1, kv, memo), dfs(j, kv, memo) + (LL)kv[i].first * kv[i].second);
    }
    long long maximumTotalDamage(vector<int>& power) {
        unordered_map<int, int> cnt;
        for (int x : power) cnt[x]++;
        vector<pair<int, int>> kv(cnt.begin(), cnt.end());
        sort(kv.begin(), kv.end());
        int m = kv.size();
        vector<LL> memo(m, -1);
        return dfs(m - 1, kv, memo);
    }
};

// class Solution : public Solution1 {};

class Solution : public Solution2 {};

// @lc code=end
