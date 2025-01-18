/*
 * @lc app=leetcode.cn id=2501 lang=cpp
 *
 * [2501] 数组中最长的方波
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int longestSquareStreak(vector<int>& nums) {
        unordered_set<long long> st(nums.begin(), nums.end());
        int ans = 0;
        for (int x : nums) {
            long long tmp = x;
            int cnt = 0;
            while (st.find(tmp) != st.end()) {
                cnt++;
                tmp *= tmp;
            }
            ans = max(ans, cnt);
        }
        return ans >= 2 ? ans : -1;
    }
};

class Solution2 {
public:
    int longestSquareStreak(vector<int>& nums) {
        sort(nums.begin(), nums.end(), greater<int>());
        unordered_map<long long, int> f;
        int ans = 0;
        for (int x : nums) {
            if (f.count(1LL * x * x)) {
                f[x] = f[1LL * x * x] + 1;
            } else {
                f[x] = 1;
            }
            ans = max(ans, f[x]);
        }
        return ans >= 2 ? ans : -1;
    }
};

class Solution3 {
public:
    int longestSquareStreak(vector<int>& nums) {
        unordered_set<long long> st(nums.begin(), nums.end());
        vector<int> memo(1e5 + 1, -1);
        auto dfs = [&](auto&& dfs, long long x) -> int {
            if (x > 1e5) return 0;
            int &res = memo[x];
            if (res != -1) return res;
            if (!st.count(x)) return res = 0;
            return res = 1 + dfs(dfs, x * x);
        };
        int ans = 0;
        for (int x : nums) {
            ans = max(ans, dfs(dfs, x));
        }
        return ans >= 2 ? ans : -1;
    }
};

// class Solution : public Solution1 {};
class Solution : public Solution2 {};
// class Solution : public Solution3 {};
// @lc code=end

