/*
 * @lc app=leetcode.cn id=2244 lang=cpp
 *
 * [2244] 完成所有任务需要的最少轮数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int minimumRounds(vector<int>& tasks) {
        int ans = 0;
        unordered_map<int, int> cnt;
        for (int x : tasks) cnt[x]++;
        for (auto kv : cnt) {
            int v = kv.second;
            if (v == 1) return -1;
            ans += v / 3 + (v % 3 ? 1 : 0);
        }
        return ans;
    }
};
// @lc code=end

