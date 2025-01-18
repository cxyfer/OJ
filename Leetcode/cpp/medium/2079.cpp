/*
 * @lc app=leetcode id=2079 lang=cpp
 *
 * [2079] Watering Plants
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int wateringPlants(vector<int>& plants, int capacity) {
        int n = plants.size(), ans = 0, cur = capacity;
        for (int i = 0; i < n; i++) {
            ans += 1;
            if (cur < plants[i]) { // 水不夠，要補滿
                cur = capacity;
                ans += i * 2;
            }
            cur -= plants[i];
        }
        return ans;
    }
};
// @lc code=end

