/*
 * @lc app=leetcode.cn id=1535 lang=cpp
 *
 * [1535] 找出数组游戏的赢家
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int getWinner(vector<int>& arr, int k) {
        int n = arr.size();
        if (k >= n - 1) return *max_element(arr.begin(), arr.end());
        int cur = arr[0], win = 0;
        for (int i = 1; i < n && win < k; i++) {
            if (arr[i] > cur) {
                cur = arr[i];
                win = 0;
            }
            win += 1;
        }
        return cur;
    }
};
// @lc code=end

