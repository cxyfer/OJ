/*
 * @lc app=leetcode.cn id=846 lang=cpp
 *
 * [846] 一手顺子
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        map<int, int> cnt; // ordered map
        for (int x : hand) cnt[x]++;
        for (auto it = cnt.begin(); it != cnt.end(); it++) {
            if (it->second == 0) continue;
            int need = it->second;
            for (int i = 0; i < groupSize; i++) {
                if (cnt[it->first + i] < need) return false;
                cnt[it->first + i] -= need;
            }
        }
        return true;
    }
};
// @lc code=end
