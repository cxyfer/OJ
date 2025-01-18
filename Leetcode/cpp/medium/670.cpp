/*
 * @lc app=leetcode.cn id=670 lang=cpp
 *
 * [670] 最大交换
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int maximumSwap(int num) {
        vector<int> digits;
        while (num > 0) {
            digits.push_back(num % 10);
            num /= 10;
        }
        reverse(digits.begin(), digits.end());
        int n = digits.size();
        int idx = n - 1, left = 0, right = 0;
        for (int i = n - 2; i >=0; i--) {
            if (digits[i] > digits[idx])
                idx = i;
            else if (digits[i] < digits[idx])
                left = i, right = idx;
        }
        swap(digits[left], digits[right]);
        int ans = 0;
        for (int x : digits)
            ans = ans * 10 + x;
        return ans;
    }
};
// @lc code=end

