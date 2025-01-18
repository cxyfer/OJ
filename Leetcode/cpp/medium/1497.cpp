/*
 * @lc app=leetcode.cn id=1497 lang=cpp
 *
 * [1497] 检查数组对是否可以被 k 整除
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    bool canArrange(vector<int>& arr, int k) {
        vector<int> cnt(k, 0);
        for (int x : arr) cnt[(x % k + k) % k]++;
        for (int i = 1; i < (k + 1) / 2; i++) {
            if (cnt[i] != cnt[k - i]) return false;
        }
        if (((k & 1) == 0) && cnt[k / 2] & 1) return false;
        return true;
    }
};
// @lc code=end

