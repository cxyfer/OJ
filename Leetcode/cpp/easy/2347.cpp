/*
 * @lc app=leetcode.cn id=2347 lang=cpp
 *
 * [2347] 最好的扑克手牌
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    string bestHand(vector<int>& ranks, vector<char>& suits) {
        unordered_set<char> set(suits.begin(), suits.end());
        if (set.size() == 1) return "Flush";
        unordered_map<int, int> cnt;
        for (int rk : ranks) {
            cnt[rk]++;
        }
        int r = 0;
        for (auto kv : cnt) {
            r = max(r, kv.second);
        }
        if (r >= 3) return "Three of a Kind";
        if (r == 2) return "Pair";
        return "High Card";
    }
};
// @lc code=end

