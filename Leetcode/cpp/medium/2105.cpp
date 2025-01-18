/*
 * @lc app=leetcode.cn id=2105 lang=cpp
 *
 * [2105] 给植物浇水 II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int minimumRefill(vector<int>& plants, int capacityA, int capacityB) {
        int n = plants.size();
        int ans = 0, a = capacityA, b = capacityB, i = 0, j = n - 1;
        while (i < j) {
            if (a < plants[i]) a = capacityA, ans++; // A 的水不夠，補滿 A 的水
            a -= plants[i]; i++; // A 澆水
            if (b < plants[j]) b = capacityB, ans++; // B 的水不夠，補滿 B 的水
            b -= plants[j]; j--; // B 澆水
        }
        if (i == j && max(a, b) < plants[i]) ans++; // 相遇時兩人的水都不夠，需要補水
        return ans;
    }
};
// @lc code=end

